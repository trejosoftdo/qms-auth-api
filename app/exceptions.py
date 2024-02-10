"""Exceptions"""

from fastapi import status
from fastapi import HTTPException
from . import constants


INTERNAL_SERVER_ERROR = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail=constants.INTERNAL_SERVER_ERROR_MESSAGE,
)

INVALID_TOKEN_ERROR = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=constants.INVALID_TOKEN_ERROR_MESSAGE,
)

FORBIDDEN_ERROR = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail=constants.FORBIDDEN_ERROR_MESSAGE,
)

UNAUTHORIZED_ERROR = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=constants.UNAUTHORIZED_ERROR_MESSAGE,
)

NOT_FOUND_ERROR = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail=constants.NOT_FOUND_ERROR_MESSAGE,
)
