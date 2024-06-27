from beanie import Document

class LoginRequestBody(Document):
  username: str
  password: str

  class Config:
    json_schema_extra = {
      "example": {
        "username": "johndoe2024",
        "password": "test1234!"
      }
    }