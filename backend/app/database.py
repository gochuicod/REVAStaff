from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.user import User
from app.models.auth import LoginRequestBody
from dotenv import dotenv_values

config = dotenv_values(".env")
MONGODB_URI = config['MONGODB_URI']
MONGODB_NAME = config['MONGODB_NAME']

async def init_db():
  try:
    client = AsyncIOMotorClient(MONGODB_URI)
    db = client[MONGODB_NAME]

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
