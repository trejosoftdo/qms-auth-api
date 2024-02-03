"""Status API router"""

from fastapi import APIRouter, Depends
from .. import helpers
from .. import constants
from .constants import (
    TAGS,
    ADD_STATUS_OPERATION_ID,
    DELETE_STATUS_BY_ID_OPERATION_ID,
    GET_STATUSES_OPERATION_ID,
    GET_STATUS_BY_ID_OPERATION_ID,
    PATCH_STATUS_OPERATION_ID,
    UPDATE_STATUS_OPERATION_ID,
)
from . import handlers
from . import models


router = APIRouter()


@router.get(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_STATUSES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_STATUSES_OPERATION_ID,
    response_model=models.StatusesListResponse,
)
def get_statuses(
    active: bool = True,
    offset: int = 0,
    limit: int = 10,
) -> models.StatusesListResponse:
    """
    Gets a list of statuses
    """
    return handlers.get_statuses(active, offset, limit)


@router.get(
    "/{status_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_STATUSES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_STATUS_BY_ID_OPERATION_ID,
    response_model=models.Status,
)
def get_status_by_id(status_id: int) -> models.Status:
    """
    Get info of an existing status by Id
    """
    return handlers.get_status_by_id(status_id)


@router.post(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_STATUSES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=ADD_STATUS_OPERATION_ID,
    response_model=models.APIResponse,
)
def add_status(payload: models.CreateStatusPayload) -> models.APIResponse:
    """
    Add a new status
    """
    return handlers.add_status(payload)


@router.put(
    "/{status_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_STATUSES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=UPDATE_STATUS_OPERATION_ID,
    response_model=models.APIResponse,
)
def update_status(
    status_id: int, payload: models.UpdateStatusPayload
) -> models.APIResponse:
    """
    Update an existing status by Id
    """
    return handlers.update_status(status_id, payload)


@router.patch(
    "/{status_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_STATUSES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=PATCH_STATUS_OPERATION_ID,
    response_model=models.APIResponse,
)
def patch_status(
    status_id: int, payload: models.PatchStatusPayload
) -> models.APIResponse:
    """
    Update partially an existing status by Id
    """
    return handlers.partially_update_status(status_id, payload)


@router.delete(
    "/{status_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_STATUSES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=DELETE_STATUS_BY_ID_OPERATION_ID,
    response_model=models.APIResponse,
)
def delete_status_by_id(status_id: int) -> models.APIResponse:
    """
    Delete an existing status by Id
    """
    return handlers.get_status_by_id(status_id)
