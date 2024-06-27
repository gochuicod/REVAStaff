"""
  Initializes the FastAPI application for REVAStaff API with routers and asynchronous context manager for database initialization.

  Imports:
  - from fastapi import FastAPI: Importing FastAPI framework for building APIs.
  - from contextlib import asynccontextmanager: Importing asynccontextmanager for defining asynchronous context managers.
  - from config.database import init_db: Importing function for initializing the database.
  - from routes.user_router import user: Importing user router for handling user-related endpoints.
  - from routes.authentication_router import authentication: Importing authentication router for handling authentication endpoints.

  Functions:
  - async def lifespan(app: FastAPI): Asynchronous context manager for initializing the database when the application starts and printing a message when shutting down.

  Initialization:
  - app: FastAPI instance initialized with title, description, version, and lifespan set to the defined async context manager.
  - app.include_router(user, tags=["Users"], prefix="/api/users"): Includes user router with '/api/users' prefix and 'Users' tag.
  - app.include_router(authentication, tags=["Authentication"], prefix="/api/auth"): Includes authentication router with '/api/auth' prefix and 'Authentication' tag.
"""

# from os import getenv
# from fastapi import FastAPI, Request
# from fastapi.middleware.cors import CORSMiddleware
# from typing import Callable

# from src.config.database import init_db
# from src.routes.user_router import user
# from src.routes.authentication_router import authentication

# app = FastAPI(
#   title="REVAStaff API",
#   description="This API backend powers a sophisticated wiki platform for REVAStaff, \
#             designed to streamline knowledge management within the organization. \
#             It provides robust API endpoints for creating, editing, and retrieving \
#             wiki documents securely. Built with efficiency in mind, it ensures seamless \
#             integration with user authentication and authorization systems, guaranteeing \
#             only authorized personnel access critical information. The backend leverages \
#             modern encryption standards and database technologies to maintain data integrity \
#             and confidentiality, supporting REVAStaff's commitment to efficient collaboration \
#             and knowledge sharing.",
#   version="1.0",
# )

# origins = getenv("ORIGINS", "*")
# app.add_middleware(
#   CORSMiddleware,
#   allow_origins=[origins] if origins != "*" else ["*"],
#   allow_credentials=True,
#   allow_methods=["*"],
#   allow_headers=["*"],
# )

# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next: Callable):
#   await init_db()
#   response = await call_next(request)
#   return response

# app.include_router(user, tags=["Users"], prefix="/api/users")
# app.include_router(authentication, tags=["Authentication"], prefix="/api/auth")

# if __name__ == "__main__":
#   import uvicorn
#   uvicorn.run(app, host="0.0.0.0", port=8000)