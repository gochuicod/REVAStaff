from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from dotenv import load_dotenv
from os import getenv

from app.models.user import User
from app.models.auth import LoginRequestBody

load_dotenv()
MONGODB_URI = getenv('MONGODB_URI')
MONGODB_NAME = getenv('MONGODB_NAME')

async def init_db():
  try:
    mongo_client = MongoClient(MONGODB_URI)
    motor_client = AsyncIOMotorClient(mongo_client)
    db = motor_client[MONGODB_NAME]

    await init_beanie(
      database=db,
      document_models=[
        User,
        LoginRequestBody
      ]
    )
    print("Database initialized successfully.")
  except Exception as e:
    print(f"Failed to initialize database: {e}")
