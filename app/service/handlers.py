"""Service API handlers"""

from sqlalchemy.orm import Session
from .. import base_api_models
from .. import api_responses
from ..database import models as db_models
from .. import enums
from .. import mappers as general_mappers
from . import models as service_api_models
from . import mappers
from . import service


# pylint: disable=W0613


def get_services(
    session: Session, active: bool, offset: int, limit: int
) -> service_api_models.ServicesListResponse:
    """Get list of services

    Args:
        session (Session):  Database session
        active (bool): Flag to return only active records.
        offset (int): The items to skip before collecting the result set.
        limit (int): The items to return.

    Returns:
        ServicesListResponse: List of services
    """
    items = db_models.Service.find_paginated(
        session, limit, offset, lambda x: x.where(db_models.Service.is_active == active)
    )
    return list(map(general_mappers.map_service, items))


def get_service_by_id(session: Session, service_id: int) -> base_api_models.Service:
    """Get info of an existing service by Id

    Args:
        session (Session):  Database session
        service_id (int): id of the service

    Returns:
        Service: Service for id
    """
    item = db_models.Service.find_by_id(session, service_id)
    return general_mappers.map_service(item)


def delete_service_by_id(
    session: Session, service_id: int
) -> base_api_models.APIResponse:
    """Delete an existing service by Id

    Args:
        session (Session):  Database session
        service_id (int): id of the service

    Returns:
        APIResponse: The result of the deletion
    """
    db_models.Service.delete_by_id(session, service_id)
    return api_responses.ITEM_DELETED_RESPONSE


def add_service(
    session: Session, payload: service_api_models.CreateServicePayload
) -> base_api_models.APIResponse:
    """Add a new service

    Args:
        session (Session):  Database session
        payload (CreateServicePayload): payload to create service

    Returns:
        APIResponse: The result of the addition
    """
    db_models.Status.validate_status_type(
        session, payload.statusId, enums.StatusType.SERVICE
    )
    db_models.Service.create_from_data(session, payload.dict())
    return api_responses.ITEM_ADDED_RESPONSE


def update_service(
    session: Session, service_id: int, payload: service_api_models.UpdateServicePayload
) -> base_api_models.APIResponse:
    """Update an existing service by Id

    Args:
        session (Session):  Database session
        service_id (int): id of the service to update
        payload (UpdateServicePayload): payload to update service

    Returns:
        APIResponse: The result of the update
    """
    db_models.Status.validate_status_type(
        session, payload.statusId, enums.StatusType.SERVICE
    )
    db_models.Service.update_by_id(session, service_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE


def partially_update_service(
    session: Session, service_id: int, payload: service_api_models.PatchServicePayload
) -> base_api_models.APIResponse:
    """Partially updates an existing service by Id

    Args:
        session (Session):  Database session
        service_id (int): id of the service to partially update
        payload (PatchServicePayload): payload to update service

    Returns:
        APIResponse: The result of the update
    """
    if not payload.statusId is None:
        db_models.Status.validate_status_type(
            session, payload.statusId, enums.StatusType.SERVICE
        )

    db_models.Service.update_by_id(session, service_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE


def create_service_turn(
    session: Session,
    application: str,
    service_id: int,
    item: service_api_models.CreateServiceTurnPayload,
) -> service_api_models.CreateServiceTurnResponse:
    """Creates a service turn for the given service

    Args:
        session (Session):  Database session
        application (str, optional): The application in context.
        service_id (int): ID of service to create a turn from
        item (models.CreateServiceTurnPayload): The required payload

    Returns:
        CreateServiceTurnResponse: Created service turn
    """
    item = service.create_service_turn(
        session,
        application,
        service_id,
        item,
    )
    return mappers.map_service_turn_response(item)
