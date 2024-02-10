"""Exceptions"""

from fastapi import status
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
