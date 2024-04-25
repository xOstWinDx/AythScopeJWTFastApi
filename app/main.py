import time

from fastapi import FastAPI, Depends
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.auth.dependencies import get_current_active_user
from app.exceptions import MyException

from app.pages.router import router as page_router
from app.exc.router import router as exc_router
from app.auth.router import router as auth_router
from app.files.router import router as file_router

app = FastAPI(
    title="Моё приложение",
)
app.include_router(file_router)
app.include_router(exc_router)
app.include_router(page_router)
app.include_router(auth_router)


@app.exception_handler(MyException)
async def myhandlerexeption(request: Request, exc: MyException):
    return JSONResponse(status_code=400, content={"massage": "ТЫ ВЫЗВАЛ ОШИБКУ!!!!"})


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
