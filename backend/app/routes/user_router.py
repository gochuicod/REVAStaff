from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_users():
  return {"message": "List of users"}

@router.get("/{user_id}")
async def read_user(user_id: str):
  return {"message": f"User {user_id}"}