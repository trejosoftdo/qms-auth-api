"""ServiceTurn API router"""

from fastapi import APIRouter, Depends
from .. import base_api_models
from .. import constants
from .. import helpers
from .constants import (
    TAGS,
    ADD_SERVICE_TURN_OPERATION_ID,
    DELETE_SERVICE_TURN_BY_ID_OPERATION_ID,
    GET_SERVICE_TURNS_OPERATION_ID,
    GET_SERVICE_TURN_BY_ID_OPERATION_ID,
    PATCH_SERVICE_TURN_OPERATION_ID,
    UPDATE_SERVICE_TURN_OPERATION_ID,
)
from . import handlers
from . import models as service_turn_api_models


router = APIRouter()


@router.get(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_SERVICE_TURNS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_SERVICE_TURNS_OPERATION_ID,
    response_model=service_turn_api_models.ServiceTurnsListResponse,
)
def get_service_turns(
    active: bool = True,
    offset: int = 0,
    limit: int = 10,
) -> service_turn_api_models.ServiceTurnsListResponse:
    """
    Gets a list of service turns
    """
    return handlers.get_service_turns(active, offset, limit)


@router.get(
    "/{service_turn_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_SERVICE_TURNS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_SERVICE_TURN_BY_ID_OPERATION_ID,
    response_model=base_api_models.ServiceTurn,
)
def get_service_turn_by_id(service_turn_id: int) -> base_api_models.ServiceTurn:
    """
    Get info of an existing service turn by Id
    """
    return handlers.get_service_turn_by_id(service_turn_id)


@router.post(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_SERVICE_TURNS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=ADD_SERVICE_TURN_OPERATION_ID,
    response_model=base_api_models.APIResponse,
)
def add_service_turn(
    payload: service_turn_api_models.CreateServiceTurnPayload,
) -> base_api_models.APIResponse:
    """
    Add a new service turn
    """
    return handlers.add_service_turn(payload)


@router.put(
    "/{service_turn_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_SERVICE_TURNS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=UPDATE_SERVICE_TURN_OPERATION_ID,
    response_model=base_api_models.APIResponse,
)
def update_service_turn(
    service_turn_id: int, payload: service_turn_api_models.UpdateServiceTurnPayload
) -> base_api_models.APIResponse:
    """
    Update an existing service_turn by Id
    """
    return handlers.update_service_turn(service_turn_id, payload)


@router.patch(
    "/{service_turn_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_SERVICE_TURNS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=PATCH_SERVICE_TURN_OPERATION_ID,
    response_model=base_api_models.APIResponse,
)
def patch_service_turn(
    service_turn_id: int, payload: service_turn_api_models.PatchServiceTurnPayload
) -> base_api_models.APIResponse:
    """
    Update partially an existing service turn by Id
    """
    return handlers.partially_update_service_turn(service_turn_id, payload)


@router.delete(
    "/{service_turn_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_SERVICE_TURNS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=DELETE_SERVICE_TURN_BY_ID_OPERATION_ID,
    response_model=base_api_models.APIResponse,
)
def delete_service_turn_by_id(service_turn_id: int) -> base_api_models.APIResponse:
    """
    Delete an existing service turn by Id
    """
    return handlers.delete_service_turn_by_id(service_turn_id)
