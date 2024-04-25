from fastapi import HTTPException


class MyException(HTTPException):
    status_code = 500
    detail = "exception"

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)
