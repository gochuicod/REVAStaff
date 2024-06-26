"""
  Initializes the FastAPI application for REVAStaff API with routers and asynchronous context manager for database initialization.

  Imports:
  - from fastapi import FastAPI: Importing FastAPI framework for building APIs.
  - from contextlib import asynccontextmanager: Importing asynccontextmanager for defining asynchronous context managers.
  - from config.database import init_db: Importing function for initializing the database.
  - from routes.user_router import user: Importing user router for handling user-related endpoints.
  - from routes.authentication_router import authentication: Importing authentication router for handling authentication endpoints.

  Functions:
  - async def lifespan(main: FastAPI): Asynchronous context manager for initializing the database when the application starts and printing a message when shutting down.

  Initialization:
  - main: FastAPI instance initialized with title, description, version, and lifespan set to the defined async context manager.
  - main.include_router(user, tags=["Users"], prefix="/api/users"): Includes user router with '/api/users' prefix and 'Users' tag.
  - main.include_router(authentication, tags=["Authentication"], prefix="/api/auth"): Includes authentication router with '/api/auth' prefix and 'Authentication' tag.
"""

from os import getenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from config.database import init_db

from routes.user_router import user
from routes.authentication_router import authentication

@asynccontextmanager
async def lifespan(main: FastAPI):
    await init_db()
    print("Database initialized")
    yield
    print("Application is shutting down")

main = FastAPI(
  title="REVAStaff API",
  description="This API backend powers a sophisticated wiki platform for REVAStaff, \
              designed to streamline knowledge management within the organization. \
              It provides robust API endpoints for creating, editing, and retrieving \
              wiki documents securely. Built with efficiency in mind, it ensures seamless \
              integration with user authentication and authorization systems, guaranteeing \
              only authorized personnel access critical information. The backend leverages \
              modern encryption standards and database technologies to maintain data integrity \
              and confidentiality, supporting REVAStaff's commitment to efficient collaboration \
              and knowledge sharing.",
  version="1.0",
  lifespan=lifespan
)

main.add_middleware(
    CORSMiddleware,
    allow_origins=[getenv("ORIGINS")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

main.include_router(user, tags=["Users"], prefix="/api/users")
main.include_router(authentication, tags=["Authentication"], prefix="/api/auth")