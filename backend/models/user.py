"""
  Defines a Beanie document model `User` representing user data in a MongoDB collection. The model includes fields for `username`, `first_name`, `last_name`, `password`, `role`, `created_at`, and `updated_at`, along with additional configurations.

  ## Class: User
  - **Fields**:
    - `username`: Indexed string field annotated with `Indexed(unique=True)`, ensuring uniqueness across documents.
    - `first_name`: String field representing the user's first name.
    - `last_name`: String field representing the user's last name.
    - `password`: String field representing the user's password.
    - `role`: String field representing the user's role, defaulting to `"user"`.
    - `created_at`: DateTime field representing the user's creation timestamp, defaulting to the current date and time when the document is created.
    - `updated_at`: DateTime field representing the user's last update timestamp, also defaulting to the current date and time.

  - **Settings**:
    - `name`: Specifies the collection name as `"users"`.

  - **Configurations**:
    - `json_schema_extra`: Provides an example JSON structure for documentation and validation purposes, demonstrating the expected format of data.

  ### Example JSON Schema:
  ```json
  {
    "username": "johndoe2024",
    "first_name": "John",
    "last_name": "Doe",
    "password": "test1234!",
    "role": "user"
  }
"""

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