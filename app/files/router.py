from typing import Annotated

from fastapi import APIRouter, File, Depends
from starlette.responses import RedirectResponse, Response

from app.auth.dependencies import get_current_active_user
from app.tasks.tasks import writefile

router = APIRouter(tags=["Файлы"], dependencies=[Depends(get_current_active_user)])


@router.post("/files")
def getfile(
    files: Annotated[list[bytes], File(description="Добавление своих файлов")]
) -> Response:
    writefile.delay(files)
    return RedirectResponse("/", status_code=304)
