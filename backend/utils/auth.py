"""
  Defines authentication utilities and middleware for token-based authentication using JWT with FastAPI.
  Includes functions for hashing passwords, verifying passwords, creating access tokens, and retrieving current user information.

  Dependencies:
  - passlib.context.CryptContext: Password hashing context using bcrypt.
  - datetime.datetime, datetime.timedelta: Date and time operations for token expiration.
  - jose.jwt: JSON Web Token library for encoding and decoding JWTs.
  - dotenv.load_dotenv, os.getenv: Loading environment variables for token settings and secret key.

  Imports:
  - from fastapi import Depends, HTTPException, status
  - from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
  - from models.user import User: User model for database operations.

  Environment Variables:
  - ACCESS_TOKEN_EXPIRES_WEEKS: Expiration period for access tokens (weeks).
  - SECRET_KEY: Secret key for JWT encryption.
  - ALGORITHM: Algorithm used for JWT encoding.

  Functions:
  - get_current_user: Dependency function to retrieve current user based on JWT token.
  - hash_pw: Function to hash passwords using bcrypt.
  - verify_password: Function to verify plain passwords against hashed passwords.
  - create_access_token: Function to create JWT access tokens with expiration time.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from dotenv import load_dotenv
from os import getenv

from models.user import User

load_dotenv()
ACCESS_TOKEN_EXPIRES_WEEKS = getenv("ACCESS_TOKEN_EXPIRES_WEEKS")
SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")

security = HTTPBearer()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
  token = credentials.credentials
  
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: str = payload.get("sub")
    if username is None:
      raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"}
      )
  except JWTError:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid authentication credentials",
      headers={"WWW-Authenticate": "Bearer"},
    )

  user = await User.find_one(User.username == username)

  if user is None:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="User not found"
    )

  return {
    "user": user,
    "token": token
  }

def hash_pw(password: str) -> str:
  return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta):
  to_encode = data.copy()
  expire = datetime.utcnow() + expires_delta
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt