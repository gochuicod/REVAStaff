from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPAuthorizationCredentials

from datetime import timedelta

from models.user import User
from models.auth import LoginRequestBody

from utils.auth import verify_password, create_access_token, get_current_user

from config import settings

authentication = APIRouter()

@authentication.post('/login', status_code=status.HTTP_200_OK)
async def login(data: LoginRequestBody) -> dict:
  user = await User.find_one(User.username == data.username)

  if user is None or verify_password(data.password, user.password) is False:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid login credentials",
    )

  access_token_expires = timedelta(weeks=int(settings.ACCESS_TOKEN_EXPIRES_WEEKS))
  access_token = create_access_token(
    data={"sub": user.username},
    expires_delta=access_token_expires
  )

  return {"access_token": access_token, "token_type": "bearer", "detail": "User logged in!"}

@authentication.get('/users/me', status_code=status.HTTP_200_OK)
async def current_user(current_user: HTTPAuthorizationCredentials = Depends(get_current_user)) -> dict:
  return current_user