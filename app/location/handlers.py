"""Location API handlers"""

from sqlalchemy.orm import Session
from .. import base_api_models
from .. import api_responses
from ..database import models as db_models
from .. import mappers
from . import models as location_api_models


def get_locations(
    session: Session,
    active: bool,
    offset: int,
    limit: int
) -> location_api_models.LocationsListResponse:
    """Get list of locations

    Args:
        session (Session): Database session
        active (bool): Flag to return only active records.
        offset (int): The items to skip before collecting the result set.
        limit (int): The items to return.

    Returns:
        LocationsListResponse: List of locations
    """
    items = db_models.Location.find_paginated(
        session,
        limit,
        offset,
        lambda x: x.where(db_models.Location.is_active == active)
    )
    return list(map(mappers.map_location, items))


def get_location_by_id(session: Session, location_id: int) -> base_api_models.Location:
    """Get info of an existing location by Id

    Args:
        session (Session): Database session
        location_id (int): id of the location

    Returns:
        Location: Location for id
    """
    item = db_models.Location.find_by_id(session, location_id)
    return mappers.map_location(item)


def delete_location_by_id(session: Session, location_id: int) -> base_api_models.APIResponse:
    """Delete an existing location by Id

    Args:
        session (Session): Database session
        location_id (int): id of the location

    Returns:
        APIResponse: The result of the deletion
    """
    db_models.Location.delete_by_id(session, location_id)
    return api_responses.ITEM_DELETED_RESPONSE


def add_location(session: Session, payload: location_api_models.CreateLocationPayload) -> base_api_models.APIResponse:
    """Add a new location

    Args:
        session (Session): Database session
        payload (CreateLocationPayload): payload to create location

    Returns:
        APIResponse: The result of the addition
    """
    db_models.Location.create_from_data(session, payload.dict())
    return api_responses.ITEM_ADDED_RESPONSE


def update_location(
    session: Session,
    location_id: int,
    payload: location_api_models.UpdateLocationPayload
) -> base_api_models.APIResponse:
    """Update an existing location by Id

    Args:
        session (Session): Database session
        location_id (int): id of the location to update
        payload (UpdateLocationPayload): payload to update location

    Returns:
        APIResponse: The result of the update
    """
    db_models.Location.update_by_id(session, location_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE


def partially_update_location(
    session: Session,
    location_id: int,
    payload: location_api_models.PatchLocationPayload
) -> base_api_models.APIResponse:
    """Partially updates an existing location by Id

    Args:
        session (Session): Database session
        location_id (int): id of the location to partially update
        payload (PatchLocationPayload): payload to update location

    Returns:
        APIResponse: The result of the update
    """
    db_models.Location.update_by_id(session, location_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE
