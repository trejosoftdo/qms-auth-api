"""Priority API router"""

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from .. import api_responses
from .. import base_api_models
from .. import constants
from .. import helpers
from ..database import main
from .constants import (
    TAGS,
    ADD_PRIORITY_OPERATION_ID,
    DELETE_PRIORITY_BY_ID_OPERATION_ID,
    GET_PRIORITIES_OPERATION_ID,
    GET_PRIORITY_BY_ID_OPERATION_ID,
    PATCH_PRIORITY_OPERATION_ID,
    UPDATE_PRIORITY_OPERATION_ID,
)
from . import handlers
from . import models as priority_api_models


router = APIRouter()


@router.get(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_PRIORITIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_PRIORITIES_OPERATION_ID,
    response_model=priority_api_models.PrioritiesListResponse,
    responses=api_responses.responses_descriptions,
)
def get_priorities(
    active: bool = True,
    offset: int = Query(default=constants.DEFAULT_PAGE_OFFSET, ge=0),
    limit: int = Query(default=constants.DEFAULT_PAGE_LIMIT, ge=1),
    session: Session = Depends(main.get_session),
) -> priority_api_models.PrioritiesListResponse:
    """
    Gets a list of priorities
    """
    return handlers.get_priorities(session, active, offset, limit)


@router.get(
    "/{priority_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_PRIORITIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_PRIORITY_BY_ID_OPERATION_ID,
    response_model=base_api_models.Priority,
    responses=api_responses.responses_descriptions,
)
def get_priority_by_id(
    priority_id: int, session: Session = Depends(main.get_session)
) -> base_api_models.Priority:
    """
    Get info of an existing priority by Id
    """
    return handlers.get_priority_by_id(session, priority_id)


@router.post(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_PRIORITIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=ADD_PRIORITY_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    status_code=status.HTTP_201_CREATED,
    responses=api_responses.responses_descriptions,
)
def add_priority(
    payload: priority_api_models.CreatePriorityPayload,
    session: Session = Depends(main.get_session),
) -> base_api_models.APIResponse:
    """
    Add a new priority
    """
    return handlers.add_priority(session, payload)


@router.put(
    "/{priority_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_PRIORITIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=UPDATE_PRIORITY_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def update_priority(
    priority_id: int,
    payload: priority_api_models.UpdatePriorityPayload,
    session: Session = Depends(main.get_session),
) -> base_api_models.APIResponse:
    """
    Update an existing priority by Id
    """
    return handlers.update_priority(session, priority_id, payload)


@router.patch(
    "/{priority_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_PRIORITIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=PATCH_PRIORITY_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def patch_priority(
    priority_id: int,
    payload: priority_api_models.PatchPriorityPayload,
    session: Session = Depends(main.get_session),
) -> base_api_models.APIResponse:
    """
    Update partially an existing priority by Id
    """
    return handlers.partially_update_priority(session, priority_id, payload)


@router.delete(
    "/{priority_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_PRIORITIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=DELETE_PRIORITY_BY_ID_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def delete_priority_by_id(
    priority_id: int, session: Session = Depends(main.get_session)
) -> base_api_models.APIResponse:
    """
    Delete an existing priority by Id
    """
    return handlers.delete_priority_by_id(session, priority_id)
