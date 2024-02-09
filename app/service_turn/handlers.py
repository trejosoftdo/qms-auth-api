"""ServiceTurn API handlers"""

from .. import base_api_models
from .. import api_responses
from ..database import models as db_models
from .. import mappers
from . import models as service_turn_api_models


def get_service_turns(
    offset: int, limit: int
) -> service_turn_api_models.ServiceTurnsListResponse:
    """Get list of service_turns

    Args:
        active (bool): Flag to return only active records.
        offset (int): The items to skip before collecting the result set.
        limit (int): The items to return.

    Returns:
        ServiceTurnsListResponse: List of service turns
    """
    items = db_models.ServiceTurn.find_paginated(limit, offset)
    return list(map(mappers.map_service_turn, items))


def get_service_turn_by_id(service_turn_id: int) -> base_api_models.ServiceTurn:
    """Get info of an existing service_turn by Id

    Args:
        service_turn_id (int): id of the service turn

    Returns:
        ServiceTurn: ServiceTurn for id
    """
    item = db_models.ServiceTurn.find_by_id(service_turn_id)
    return mappers.map_service_turn(item)


def delete_service_turn_by_id(service_turn_id: int) -> base_api_models.APIResponse:
    """Delete an existing service_turn by Id

    Args:
        service_turn_id (int): id of the service_turn

    Returns:
        APIResponse: The result of the deletion
    """
    db_models.ServiceTurn.delete_by_id(service_turn_id)
    return api_responses.ITEM_DELETED_RESPONSE


def add_service_turn(
    payload: service_turn_api_models.CreateServiceTurnPayload,
) -> base_api_models.APIResponse:
    """Add a new service_turn

    Args:
        payload (CreateServiceTurnPayload): payload to create service_turn

    Returns:
        APIResponse: The result of the addition
    """
    db_models.ServiceTurn.create_from_data(payload.dict())
    return api_responses.ITEM_ADDED_RESPONSE


def update_service_turn(
    service_turn_id: int, payload: service_turn_api_models.UpdateServiceTurnPayload
) -> base_api_models.APIResponse:
    """Update an existing service_turn by Id

    Args:
        service_turn_id (int): id of the service_turn to update
        payload (UpdateServiceTurnPayload): payload to update service_turn

    Returns:
        APIResponse: The result of the update
    """
    db_models.ServiceTurn.update_by_id(service_turn_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE


def partially_update_service_turn(
    service_turn_id: int, payload: service_turn_api_models.PatchServiceTurnPayload
) -> base_api_models.APIResponse:
    """Partially updates an existing service_turn by Id

    Args:
        service_turn_id (int): id of the service_turn to partially update
        payload (PatchServiceTurnPayload): payload to update service_turn

    Returns:
        APIResponse: The result of the update
    """
    db_models.ServiceTurn.update_by_id(service_turn_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE
