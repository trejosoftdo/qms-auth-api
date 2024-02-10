"""Exceptions"""

from fastapi import status, HTTPException
from . import base_api_models
from . import constants

# pylint: disable=C0301

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
        "description": "Client is sending an incorrect format of API request",
    },
    422: {
        "model": base_api_models.APIResponse,
        "description": "The server was unable to process the request because it contains invalid data",
    },
    401: {
        "model": base_api_models.APIResponse,
        "description": "Client is not authenticated against the API",
    },
    403: {
        "model": base_api_models.APIResponse,
        "description": "Client doesn't have permission to request this resource",
    },
    404: {
        "model": base_api_models.APIResponse,
        "description": "Resource could not be found",
    },
    409: {
        "model": base_api_models.APIResponse,
        "description": "Request could not be processed because of conflict in the current state of the resource",
    },
    500: {
        "model": base_api_models.APIResponse,
        "description": "Unexpected internal error",
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
