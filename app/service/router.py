"""Service API router"""

from fastapi import APIRouter, Depends, Header, Query, status
from sqlalchemy.orm import Session
from .. import api_responses
from .. import constants
from .. import base_api_models
from ..database import main
from .constants import (
    TAGS,
    CREATE_SERVICE_TURN_OPERATION_ID,
    GET_SERVICES_OPERATION_ID,
    GET_SERVICE_BY_ID_OPERATION_ID,
    DELETE_SERVICE_BY_ID_OPERATION_ID,
    ADD_SERVICE_OPERATION_ID,
    UPDATE_SERVICE_OPERATION_ID,
    PATCH_SERVICE_OPERATION_ID,
)
from .. import helpers
from . import handlers
from . import models as service_api_models


router = APIRouter()


@router.get(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_SERVICES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_SERVICES_OPERATION_ID,
    response_model=service_api_models.ServicesListResponse,
    responses=api_responses.responses_descriptions,
)
def get_services(
    active: bool = True,
    offset: int = Query(default=constants.DEFAULT_PAGE_OFFSET, ge=0),
    limit: int = Query(default=constants.DEFAULT_PAGE_LIMIT, ge=1),
    session: Session = Depends(main.get_session),
) -> service_api_models.ServicesListResponse:
    """Gets a list of services for the application in context"""
    return handlers.get_services(session, active, offset, limit)


@router.get(
    "/{service_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_SERVICES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_SERVICE_BY_ID_OPERATION_ID,
    response_model=base_api_models.Service,
    responses=api_responses.responses_descriptions,
)
def get_service_by_id(service_id: int, session: Session = Depends(main.get_session)) -> base_api_models.Service:
    """
    Get info of an existing service by Id
    """
    return handlers.get_service_by_id(session, service_id)


@router.post(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_SERVICES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=ADD_SERVICE_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    status_code=status.HTTP_201_CREATED,
    responses=api_responses.responses_descriptions,
)
def add_service(
    payload: service_api_models.CreateServicePayload,
    session: Session = Depends(main.get_session),
) -> base_api_models.APIResponse:
    """
    Add a new service
    """
    return handlers.add_service(session, payload)


@router.put(
    "/{service_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_SERVICES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=UPDATE_SERVICE_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def update_service(
    service_id: int,
    payload: service_api_models.UpdateServicePayload,
    session: Session = Depends(main.get_session),
) -> base_api_models.APIResponse:
    """
    Update an existing service by Id
    """
    return handlers.update_service(session, service_id, payload)


@router.patch(
    "/{service_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_SERVICES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=PATCH_SERVICE_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def patch_service(
    service_id: int,
    payload: service_api_models.PatchServicePayload,
    session: Session = Depends(main.get_session),
) -> base_api_models.APIResponse:
    """
    Update partially an existing service by Id
    """
    return handlers.partially_update_service(session, service_id, payload)


@router.delete(
    "/{service_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_SERVICES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=DELETE_SERVICE_BY_ID_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def delete_service_by_id(service_id: int, session: Session = Depends(main.get_session),) -> base_api_models.APIResponse:
    """
    Delete an existing service by Id
    """
    return handlers.delete_service_by_id(session, service_id)


@router.post(
    "/{service_id}/serviceturns",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_SERVICE_TURNS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=CREATE_SERVICE_TURN_OPERATION_ID,
    response_model=service_api_models.CreateServiceTurnResponse,
    status_code=status.HTTP_201_CREATED,
    responses=api_responses.responses_descriptions,
)
def create_service_turn(
    service_id: int,
    item: service_api_models.CreateServiceTurnPayload,
    application: str = Header(..., convert_underscores=False),
    session: Session = Depends(main.get_session),
) -> service_api_models.CreateServiceTurnResponse:
    """Creates a service turn for the given service"""
    return handlers.create_service_turn(session, application, service_id, item)
