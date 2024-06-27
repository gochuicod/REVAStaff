from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from models.user import User
from models.auth import LoginRequestBody

from config import settings

if settings.MONGODB_URI is None or settings.MONGODB_NAME is None:
  raise HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail='Please define the MONGODB_URI and MONGODB_NAME environment variable inside .env'
  )

async def init_db():
  try:
    client = AsyncIOMotorClient(settings.MONGODB_URI)
    db = client.get_database(settings.MONGODB_NAME)

    await init_beanie(
      database=db,
      document_models=[
        User,
        LoginRequestBody
      ]
    )
  except Exception as e:
    print(e)