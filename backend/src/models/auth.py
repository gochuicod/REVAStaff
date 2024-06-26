"""
  Defines a Beanie document model `LoginRequestBody` for representing login request bodies. This model includes fields for `username` and `password` with associated JSON schema metadata.

  ## Class: LoginRequestBody
  - **Fields**:
    - `username`: String field representing the username.
    - `password`: String field representing the password.
    
  - **Configurations**:
    - `json_schema_extra`: Provides an example of the JSON structure expected for this model. This helps document the expected format of data when using APIs or documenting schemas.

  ### Example JSON Schema:
  ```json
  {
    "username": "johndoe2024",
    "password": "test1234!"
  }
"""

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