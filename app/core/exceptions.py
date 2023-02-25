from typing import Optional, Dict, Any

from fastapi import HTTPException, status


class DuplicatedError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, detail, headers)


class NotFoundError(HTTPException):
    def __init__(self, detail: Any= None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_404_NOT_FOUND, detail, headers)


class AuthError(HTTPException):
    def __init__(self, detail: Any= None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_403_FORBIDDEN, detail, headers)
