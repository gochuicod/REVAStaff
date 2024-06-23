"""
  This script initializes a connection to a MongoDB database using Beanie, an ODM (Object-Document Mapper) for MongoDB, and Motor, an async MongoDB driver. The script retrieves the MongoDB URI and database name from environment variables, establishes a connection, and initializes the Beanie models.

  ## Environment Variables:
  - `MONGODB_URI_LOCAL`: The URI for connecting to the local MongoDB instance.
  - `MONGODB_NAME`: The name of the MongoDB database to connect to.

  ## Main Components:
  1. **Environment Variable Check**:
    - Ensures that `MONGODB_URI_LOCAL` and `MONGODB_NAME` are defined.
    - If not, raises an HTTP 500 error with a relevant message.

  2. **init_db Function**:
    - Asynchronously connects to the MongoDB database using the provided URI and database name.
    - Initializes the Beanie document models, which include `User` and `LoginRequestBody`.

  ## Usage:
  To use this script, ensure that the `.env` file contains the `MONGODB_URI_LOCAL` and `MONGODB_NAME` environment variables with valid values. Then, call the `init_db` function to establish the database connection and initialize the models.

  ## Dependencies:
  - `os`: To access environment variables.
  - `fastapi`: For HTTP exceptions and status codes.
  - `motor.motor_asyncio`: To create an asynchronous MongoDB client.
  - `beanie`: For initializing Beanie with the database and document models.
  - `models.user`: Contains the `User` model.
  - `models.auth`: Contains the `LoginRequestBody` model.
"""

from os import environ
from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from models.user import User
from models.auth import LoginRequestBody

MONGODB_URI = environ.get('MONGODB_URI_LOCAL')
MONGODB_NAME = environ.get('MONGODB_NAME')

if MONGODB_URI is None or MONGODB_NAME is None:
  raise HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail='Please define the MONGODB_URI and MONGODB_NAME environment variable inside .env'
  )

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
  except Exception as e:
    print(e)