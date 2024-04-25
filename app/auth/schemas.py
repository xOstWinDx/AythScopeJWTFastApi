from pydantic import BaseModel


class SUser(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class SUserInDB(SUser):
    hashed_password: str


class STokenData(BaseModel):
    username: str | None = None


class SToken(BaseModel):
    access_token: str
    token_type: str
