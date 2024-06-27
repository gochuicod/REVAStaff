# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.user_router import router as user_router
from app.database import init_db
from dotenv import dotenv_values

config = dotenv_values(".env")
ORIGINS = config['ORIGINS'].split(" ")

app = FastAPI(
  title="FastAPI MongoDB Atlas Example",
  description="FastAPI application with MongoDB Atlas integration",
  version="1.0",
)

app.add_middleware(
  CORSMiddleware,
  allow_origins=ORIGINS,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(user_router, prefix="/api/users", tags=["Users"])

@app.on_event("startup")
async def startup_db_client():
  await init_db()

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=8000)