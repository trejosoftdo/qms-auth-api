"""Queue API router"""

from fastapi import APIRouter, Depends
from .. import base_api_models
from .. import constants
from .. import helpers
from .constants import (
    TAGS,
    ADD_QUEUE_OPERATION_ID,
    DELETE_QUEUE_BY_ID_OPERATION_ID,
    GET_QUEUES_OPERATION_ID,
    GET_QUEUE_BY_ID_OPERATION_ID,
    PATCH_QUEUE_OPERATION_ID,
    UPDATE_QUEUE_OPERATION_ID,
)
from . import handlers
from . import models as queue_api_models


router = APIRouter()


@router.get(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_QUEUES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_QUEUES_OPERATION_ID,
    response_model=queue_api_models.QueuesListResponse,
)
def get_queues(
    active: bool = True,
    offset: int = 0,
    limit: int = 10,
) -> queue_api_models.QueuesListResponse:
    """
    Gets a list of queues
    """
    return handlers.get_queues(active, offset, limit)


@router.get(
    "/{queue_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_QUEUES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_QUEUE_BY_ID_OPERATION_ID,
    response_model=base_api_models.Queue,
)
def get_queue_by_id(queue_id: int) -> base_api_models.Queue:
    """
    Get info of an existing queue by Id
    """
    return handlers.get_queue_by_id(queue_id)


@router.post(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_QUEUES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=ADD_QUEUE_OPERATION_ID,
    response_model=base_api_models.APIResponse,
)
def add_queue(
    payload: queue_api_models.CreateQueuePayload,
) -> base_api_models.APIResponse:
    """
    Add a new queue
    """
    return handlers.add_queue(payload)


@router.put(
    "/{queue_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_QUEUES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=UPDATE_QUEUE_OPERATION_ID,
    response_model=base_api_models.APIResponse,
)
def update_queue(
    queue_id: int, payload: queue_api_models.UpdateQueuePayload
) -> base_api_models.APIResponse:
    """
    Update an existing queue by Id
    """
    return handlers.update_queue(queue_id, payload)


@router.patch(
    "/{queue_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_QUEUES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=PATCH_QUEUE_OPERATION_ID,
    response_model=base_api_models.APIResponse,
)
def patch_queue(
    queue_id: int, payload: queue_api_models.PatchQueuePayload
) -> base_api_models.APIResponse:
    """
    Update partially an existing queue by Id
    """
    return handlers.partially_update_queue(queue_id, payload)


@router.delete(
    "/{queue_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_QUEUES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=DELETE_QUEUE_BY_ID_OPERATION_ID,
    response_model=base_api_models.APIResponse,
)
def delete_queue_by_id(queue_id: int) -> base_api_models.APIResponse:
    """
    Delete an existing queue by Id
    """
    return handlers.delete_queue_by_id(queue_id)
