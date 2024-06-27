from os import getenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from config.database import init_db

from routes.authentication_router import authentication
from routes.user_router import user

load_dotenv()
origins = getenv('ORIGINS').split(' ')

app = FastAPI(
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
)

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(authentication, tags=["Authentication"], prefix="/api/auth")
app.include_router(user, tags=["Users"], prefix="/api/users")

@app.on_event("startup")
async def start_db():
  await init_db()