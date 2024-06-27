from fastapi import APIRouter
from app.models.user import User

router = APIRouter()

@router.get("/")
async def read_users():
  users = await User.find_all().to_list();
  return users

@router.get("/{user_id}")
async def read_user(user_id: str):
  return {"message": f"User {user_id}"}