from os import getenv

class Settings:
  MONGODB_URI:str = getenv("MONGODB_URI")
  MONGODB_NAME:str = getenv("MONGODB_NAME")
  ACCESS_TOKEN_EXPIRES_WEEKS:str = getenv("ACCESS_TOKEN_EXPIRES_WEEKS")
  SECRET_KEY:str = getenv("SECRET_KEY")
  ALGORITHM:str = getenv("ALGORITHM")
  ORIGINS:str = getenv("ORIGINS")
  RELOAD:str = getenv("RELOAD")

settings = Settings()