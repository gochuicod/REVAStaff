from os import environ
from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from pymongo import MongoClient

from models.user import User
from models.auth import LoginRequestBody

MONGODB_URI = environ.get('MONGODB_URI')
MONGODB_NAME = environ.get('MONGODB_NAME')

if MONGODB_URI is None or MONGODB_NAME is None:
  raise HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail='Please define the MONGODB_URI and MONGODB_NAME environment variable inside .env'
  )

async def init_db():
  try:
    client = AsyncIOMotorClient(MONGODB_URI)
    db = client.get_database("revastaff")

    await init_beanie(
      database=db,
      document_models=[
        User,
        LoginRequestBody
      ]
    )
  except Exception as e:
    print(e)