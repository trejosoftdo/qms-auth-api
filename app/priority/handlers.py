"""Priority API handlers"""

from .. import base_api_models
from .. import api_responses
from ..database import models as db_models
from .. import mappers
from . import models as priority_api_models


def get_priorities(
    active: bool, offset: int, limit: int
) -> priority_api_models.PrioritiesListResponse:
    """Get list of priorities

    Args:
        active (bool): Flag to return only active records.
        offset (int): The items to skip before collecting the result set.
        limit (int): The items to return.

    Returns:
        PrioritiesListResponse: List of priorities
    """
    items = db_models.Priority.find_paginated(
        limit, offset, lambda x: x.where(db_models.Priority.is_active == active)
    )
    return list(map(mappers.map_priority, items))


def get_priority_by_id(priority_id: int) -> base_api_models.Priority:
    """Get info of an existing priority by Id

    Args:
        priority_id (int): id of the priority

    Returns:
        Priority: Priority for id
    """
    item = db_models.Priority.find_by_id(priority_id)
    return mappers.map_priority(item)


def delete_priority_by_id(priority_id: int) -> base_api_models.APIResponse:
    """Delete an existing priority by Id

    Args:
        priority_id (int): id of the priority

    Returns:
        APIResponse: The result of the deletion
    """
    db_models.Priority.delete_by_id(priority_id)
    return api_responses.ITEM_DELETED_RESPONSE


def add_priority(payload: priority_api_models.CreatePriorityPayload) -> base_api_models.APIResponse:
    """Add a new priority

    Args:
        payload (CreatePriorityPayload): payload to create priority

    Returns:
        APIResponse: The result of the addition
    """
    db_models.Priority.create_from_data(payload.dict())
    return api_responses.ITEM_ADDED_RESPONSE


def update_priority(
    priority_id: int, payload: priority_api_models.UpdatePriorityPayload
) -> base_api_models.APIResponse:
    """Update an existing priority by Id

    Args:
        priority_id (int): id of the priority to update
        payload (UpdatePriorityPayload): payload to update priority

    Returns:
        APIResponse: The result of the update
    """
    db_models.Priority.update_by_id(priority_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE


def partially_update_priority(
    priority_id: int, payload: priority_api_models.PatchPriorityPayload
) -> base_api_models.APIResponse:
    """Partially updates an existing priority by Id

    Args:
        priority_id (int): id of the priority to partially update
        payload (PatchPriorityPayload): payload to update priority

    Returns:
        APIResponse: The result of the update
    """
    db_models.Priority.update_by_id(priority_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE
