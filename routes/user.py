from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from models.model import UserModel
from classes.user import User

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(data: UserModel):
    return JSONResponse(content=data.dict(), status_code=status.HTTP_201_CREATED)
    if user.save():
        return JSONResponse(content=data.dict(), status_code=status.HTTP_201_CREATED)
    else:
        return JSONResponse(content={"msg": "Erro ao salvar"}, status_code=status.HTTP_400_BAD_REQUEST)

@router.get('/{user_id}', status_code=status.HTTP_200_OK)
async def get_user(user_id: str):
    return {"user_id": user_id}
