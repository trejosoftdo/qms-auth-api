"""Location API router"""

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from .. import api_responses
from .. import base_api_models
from .. import constants
from .. import helpers
from ..database import main
from .constants import (
    TAGS,
    ADD_LOCATION_OPERATION_ID,
    DELETE_LOCATION_BY_ID_OPERATION_ID,
    GET_LOCATIONS_OPERATION_ID,
    GET_LOCATION_BY_ID_OPERATION_ID,
    PATCH_LOCATION_OPERATION_ID,
    UPDATE_LOCATION_OPERATION_ID,
)
from . import handlers
from . import models as location_api_models


router = APIRouter()


@router.get(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_LOCATIONS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_LOCATIONS_OPERATION_ID,
    response_model=location_api_models.LocationsListResponse,
    responses=api_responses.responses_descriptions,
)
def get_locations(
    active: bool = True,
    offset: int = Query(default=constants.DEFAULT_PAGE_OFFSET, ge=0),
    limit: int = Query(default=constants.DEFAULT_PAGE_LIMIT, ge=1),
    session: Session = Depends(main.get_session),
) -> location_api_models.LocationsListResponse:
    """
    Gets a list of locations
    """
    return handlers.get_locations(session, active, offset, limit)


@router.get(
    "/{location_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_LOCATIONS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_LOCATION_BY_ID_OPERATION_ID,
    response_model=base_api_models.Location,
    responses=api_responses.responses_descriptions,
)
def get_location_by_id(
    location_id: int, session: Session = Depends(main.get_session)
) -> base_api_models.Location:
    """
    Get info of an existing location by Id
    """
    return handlers.get_location_by_id(session, location_id)


@router.post(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_LOCATIONS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=ADD_LOCATION_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    status_code=status.HTTP_201_CREATED,
    responses=api_responses.responses_descriptions,
)
def add_location(
    payload: location_api_models.CreateLocationPayload,
    session: Session = Depends(main.get_session),
) -> base_api_models.APIResponse:
    """
    Add a new location
    """
    return handlers.add_location(session, payload)


@router.put(
    "/{location_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_LOCATIONS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=UPDATE_LOCATION_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def update_location(
    location_id: int,
    payload: location_api_models.UpdateLocationPayload,
    session: Session = Depends(main.get_session),
) -> base_api_models.APIResponse:
    """
    Update an existing location by Id
    """
    return handlers.update_location(session, location_id, payload)


@router.patch(
    "/{location_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_LOCATIONS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=PATCH_LOCATION_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def patch_location(
    location_id: int,
    payload: location_api_models.PatchLocationPayload,
    session: Session = Depends(main.get_session),
) -> base_api_models.APIResponse:
    """
    Update partially an existing location by Id
    """
    return handlers.partially_update_location(session, location_id, payload)


@router.delete(
    "/{location_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_LOCATIONS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=DELETE_LOCATION_BY_ID_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def delete_location_by_id(
    location_id: int, session: Session = Depends(main.get_session)
) -> base_api_models.APIResponse:
    """
    Delete an existing location by Id
    """
    return handlers.delete_location_by_id(session, location_id)
