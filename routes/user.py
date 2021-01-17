from fastapi import APIRouter, status
from models.model import UserModel
from classes.user import User

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(data: UserModel):
    user = User(data)
    user.save()

@router.get('/{user_id}', status_code=status.HTTP_200_OK)
async def get_user(user_id: str):
    return {"user_id": user_id}
