from fastapi import APIRouter, Depends
from starlette.responses import HTMLResponse

from app.auth.dependencies import get_current_active_user

router = APIRouter(tags=["Страничка"])


@router.get("/", response_class=HTMLResponse)
async def main():
    return """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
