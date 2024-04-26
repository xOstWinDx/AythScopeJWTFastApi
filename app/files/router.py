from typing import Annotated

from fastapi import APIRouter, File, Depends, BackgroundTasks
from starlette.responses import RedirectResponse, Response, FileResponse

from app.auth.dependencies import get_current_active_user
from app.tasks.tasks import writefile

router = APIRouter(tags=["Файлы"], dependencies=[Depends(get_current_active_user)])


@router.post("/files")
def getfile(
    files: Annotated[list[bytes], File(description="Добавление своих файлов")],
    background_tasks: BackgroundTasks,
) -> Response:
    background_tasks.add_task(writefile, files)
    return RedirectResponse("/", status_code=304)


some_file_path = "app/files/myvideo.mp4"


@router.get("/file", response_class=FileResponse)
async def getfile():
    return some_file_path
