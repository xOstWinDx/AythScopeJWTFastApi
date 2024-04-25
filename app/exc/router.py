from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_active_user
from app.exceptions import MyException

router = APIRouter(tags=["Ошибки"], dependencies=[Depends(get_current_active_user)])


@router.get("/error", description="эндпоинт кидающий исключение")
async def doexception():
    raise MyException
