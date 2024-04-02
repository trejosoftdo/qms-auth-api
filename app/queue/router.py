"""Queue API router"""

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from .. import api_responses
from .. import base_api_models
from .. import constants
from .. import helpers
from ..database import main
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
    responses=api_responses.responses_descriptions,
)
def get_queues(
    active: bool = True,
    offset: int = Query(default=constants.DEFAULT_PAGE_OFFSET, ge=0),
    limit: int = Query(default=constants.DEFAULT_PAGE_LIMIT, ge=1),
    session: Session = Depends(main.get_session),
) -> queue_api_models.QueuesListResponse:
    """
    Gets a list of queues
    """
    return handlers.get_queues(session, active, offset, limit)


@router.get(
    "/{queue_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_QUEUES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_QUEUE_BY_ID_OPERATION_ID,
    response_model=base_api_models.Queue,
    responses=api_responses.responses_descriptions,
)
def get_queue_by_id(
    queue_id: int, session: Session = Depends(main.get_session)
) -> base_api_models.Queue:
    """
    Get info of an existing queue by Id
    """
    return handlers.get_queue_by_id(session, queue_id)


@router.post(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_QUEUES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=ADD_QUEUE_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    status_code=status.HTTP_201_CREATED,
    responses=api_responses.responses_descriptions,
)
def add_queue(
    payload: queue_api_models.CreateQueuePayload,
    session: Session = Depends(main.get_session),
) -> base_api_models.APIResponse:
    """
    Add a new queue
    """
    return handlers.add_queue(session, payload)


@router.put(
    "/{queue_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_QUEUES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=UPDATE_QUEUE_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def update_queue(
    queue_id: int,
    payload: queue_api_models.UpdateQueuePayload,
    session: Session = Depends(main.get_session),
) -> base_api_models.APIResponse:
    """
    Update an existing queue by Id
    """
    return handlers.update_queue(session, queue_id, payload)


@router.patch(
    "/{queue_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_QUEUES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=PATCH_QUEUE_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def patch_queue(
    queue_id: int,
    payload: queue_api_models.PatchQueuePayload,
    session: Session = Depends(main.get_session),
) -> base_api_models.APIResponse:
    """
    Update partially an existing queue by Id
    """
    return handlers.partially_update_queue(session, queue_id, payload)


@router.delete(
    "/{queue_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_QUEUES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=DELETE_QUEUE_BY_ID_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def delete_queue_by_id(
    queue_id: int, session: Session = Depends(main.get_session)
) -> base_api_models.APIResponse:
    """
    Delete an existing queue by Id
    """
    return handlers.delete_queue_by_id(session, queue_id)
