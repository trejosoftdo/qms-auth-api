"""Exceptions"""

from fastapi import status, HTTPException
from . import base_api_models
from . import constants


ITEM_DELETED_RESPONSE = base_api_models.APIResponse(
    code=status.HTTP_200_OK,
    type=constants.OPERATION_DELETE,
    message=constants.ITEM_DELETED_SUCCESSFULLY_MESSAGE,
)

ITEM_ADDED_RESPONSE = base_api_models.APIResponse(
    code=status.HTTP_201_CREATED,
    type=constants.OPERATION_ADD,
    message=constants.ITEM_ADDED_SUCCESSFULLY_MESSAGE,
)

ITEM_UPDATED_RESPONSE = base_api_models.APIResponse(
    code=status.HTTP_200_OK,
    type=constants.OPERATION_UPDATE,
    message=constants.ITEM_UPDATED_SUCCESSFULLY_MESSAGE,
)


responses_descriptions = {
    400: {
        "model": base_api_models.APIResponse,
        "description": constants.HTTP_400_DESCRIPTION,
    },
    422: {
        "model": base_api_models.APIResponse,
        "description": constants.HTTP_422_DESCRIPTION,
    },
    401: {
        "model": base_api_models.APIResponse,
        "description": constants.HTTP_401_DESCRIPTION,
    },
    403: {
        "model": base_api_models.APIResponse,
        "description": constants.HTTP_403_DESCRIPTION,
    },
    404: {
        "model": base_api_models.APIResponse,
        "description": constants.HTTP_404_DESCRIPTION,
    },
    409: {
        "model": base_api_models.APIResponse,
        "description": constants.HTTP_409_DESCRIPTION,
    },
    500: {
        "model": base_api_models.APIResponse,
        "description": constants.HTTP_500_DESCRIPTION,
    },
}


def get_validation_error_response(message: str) -> base_api_models.APIResponse:
    """Gets a validation error response

    Args:
        message (str): Message of the error

    Returns:
        base_api_models.APIResponse: Error response
    """
    return base_api_models.APIResponse(
        code=status.HTTP_400_BAD_REQUEST,
        type=constants.INVALID_REQUEST,
        message=message,
    )


def get_response_from_exception(exc: HTTPException) -> base_api_models.APIResponse:
    """Gets an error response from a HTTP Exception

    Args:
        exc (HTTPException): The Exception

    Returns:
        base_api_models.APIResponse: Error response
    """
    return base_api_models.APIResponse(
        code=exc.status_code,
        type=exc.detail["type"],
        message=exc.detail["message"],
    )
