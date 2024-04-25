from datetime import timedelta
from typing import Annotated

from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from app.auth.auth import (
    authenticate_user,
    create_access_token,
)
from app.auth.dependencies import (
    get_current_active_user,
)
from app.auth.schemas import SUser, SToken
from app.config import settings

router = APIRouter(tags=["Аутентификация"])


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> SToken:
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return SToken(access_token=access_token, token_type="bearer")


@router.get("/users/me", response_model=SUser)
async def read_users_me(
    current_user: Annotated[SUser, Depends(get_current_active_user)],
):
    return current_user
