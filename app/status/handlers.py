"""Status API handlers"""

from sqlalchemy.orm import Session
from .. import base_api_models
from .. import api_responses
from ..database import models as db_models
from .. import mappers
from . import models as status_api_models


def get_statuses(
    session: Session,
    active: bool,
    offset: int,
    limit: int
) -> status_api_models.StatusesListResponse:
    """Get list of statuses

    Args:
        session (Session): Database session
        active (bool): Flag to return only active records.
        offset (int): The items to skip before collecting the result set.
        limit (int): The items to return.

    Returns:
        StatusesListResponse: List of statuses
    """
    items = db_models.Status.find_paginated(
        session,
        limit,
        offset,
        lambda x: x.where(db_models.Status.is_active == active)
    )
    return list(map(mappers.map_status, items))


def get_status_by_id(session: Session, status_id: int) -> base_api_models.Status:
    """Get info of an existing status by Id

    Args:
        session (Session): Database session
        status_id (int): id of the status

    Returns:
        Status: Status for id
    """
    item = db_models.Status.find_by_id(session, status_id)
    return mappers.map_status(item)


def delete_status_by_id(session: Session, status_id: int) -> base_api_models.APIResponse:
    """Delete an existing status by Id

    Args:
        session (Session): Database session
        status_id (int): id of the status

    Returns:
        APIResponse: The result of the deletion
    """
    db_models.Status.delete_by_id(session, status_id)
    return api_responses.ITEM_DELETED_RESPONSE


def add_status(
    session: Session,
    payload: status_api_models.CreateStatusPayload,
) -> base_api_models.APIResponse:
    """Add a new status

    Args:
        session (Session): Database session
        payload (CreateStatusPayload): payload to create status

    Returns:
        APIResponse: The result of the addition
    """
    db_models.Status.create_from_data(session, payload.dict())
    return api_responses.ITEM_ADDED_RESPONSE


def update_status(
    session: Session,
    status_id: int,
    payload: status_api_models.UpdateStatusPayload
) -> base_api_models.APIResponse:
    """Update an existing status by Id

    Args:
        session (Session): Database session
        status_id (int): id of the status to update
        payload (UpdateStatusPayload): payload to update status

    Returns:
        APIResponse: The result of the update
    """
    db_models.Status.update_by_id(session, status_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE


def partially_update_status(
    session: Session,
    status_id: int,
    payload: status_api_models.PatchStatusPayload
) -> base_api_models.APIResponse:
    """Partially updates an existing status by Id

    Args:
        session (Session): Database session
        status_id (int): id of the status to partially update
        payload (PatchStatusPayload): payload to update status

    Returns:
        APIResponse: The result of the update
    """
    db_models.Status.update_by_id(session, status_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE
