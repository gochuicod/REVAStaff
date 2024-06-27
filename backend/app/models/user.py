from datetime import datetime
from typing import Annotated
from beanie import Document, Indexed

class User(Document):
  username: Annotated[str, Indexed(unique=True)]
  first_name: str
  last_name: str
  password: str
  role: str = "user"
  created_at: datetime = datetime.now()
  updated_at: datetime = datetime.now()

  class Settings:
    name = "users"

  class Config:
    json_schema_extra = {
      "example": {
        "username": "johndoe2024",
        "first_name": "John",
        "last_name": "Doe",
        "password": "test1234!",
        "role": "user"
      }
    }