from fastapi import HTTPException, status


class NotFoundHTTPException(HTTPException):
    def __init__(self, msg: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=msg if msg else "Requested resource is not found",
        )
