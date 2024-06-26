"""
  Defines CRUD endpoints for managing user data with authentication and authorization using FastAPI.
  Endpoints include:
  - GET '/': Retrieves all users (admin only).
  - POST '/': Creates a new user (admin only).
  - PATCH '/{id}': Updates user credentials (admin only).
  - DELETE '/{id}': Deletes a user (admin only).

  Dependencies:
  - pymongo.errors.DuplicateKeyError: Handles duplicate username errors.
  - bson.ObjectId: Handles MongoDB ObjectId for user ID.
  - models.user.User: User model for database operations.
  - utils.auth.hash_pw: Function for hashing passwords securely.
  - utils.auth.get_current_user: Dependency function for retrieving current user details.
"""

from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials

from pymongo.errors import DuplicateKeyError
from bson import ObjectId
from typing import List

from src.models.user import User

from src.utils.auth import hash_pw, get_current_user

user = APIRouter()

@user.get('/', status_code=status.HTTP_200_OK)
async def get_all_users(current_user: HTTPAuthorizationCredentials = Depends(get_current_user)) -> List[User]:
  if(current_user.get("user").role != "admin"):
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Unauthorized access."
    )
  
  users = await User.find_all().to_list()
  return users

@user.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(data: User, current_user: HTTPAuthorizationCredentials = Depends(get_current_user)) -> dict:
  if(current_user.get("user").role != "admin"):
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Unauthorized access."
    )
  
  data.password = hash_pw(data.password)

  try:
    await data.create()
  except DuplicateKeyError as e:
    print(e)
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Username provided is already associated with an existing account."
    )
  
  return {"detail": "User created successfully."}

@user.patch('/{id}', status_code=status.HTTP_200_OK)
async def update_user(id: str, data: dict, current_user: HTTPAuthorizationCredentials = Depends(get_current_user)) -> dict:
  if(current_user.get("user").role != "admin"):
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Unauthorized access."
    )
  
  user = await User.find_one(User.id == ObjectId(id))

  if data.get("password"):
        data["password"] = hash_pw(data.get("password"))

  for field, value in data.items():
      setattr(user, field, value)

  await user.save()

  return {"detail": "User credentials updated successfully."}

@user.delete('/{id}', status_code=status.HTTP_200_OK)
async def delete_user(id: str, current_user: HTTPAuthorizationCredentials = Depends(get_current_user)) -> dict:
  if(current_user.get("user").role != "admin"):
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Unauthorized access."
    )
  
  user = await User.find_one(User.id == ObjectId(id))

  await user.delete()

  return {"detail": "User deleted successfully."}