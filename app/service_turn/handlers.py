"""ServiceTurn API handlers"""

from .. import base_api_models
from .. import mocks
from . import models as service_turn_api_models

# pylint: disable=W0613


def get_service_turns(
    active: bool, offset: int, limit: int
) -> service_turn_api_models.ServiceTurnsListResponse:
    """Get list of service_turns

    Args:
        active (bool): Flag to return only active records.
        offset (int): The items to skip before collecting the result set.
        limit (int): The items to return.

    Returns:
        ServiceTurnsListResponse: List of service turns
    """
    return [mocks.turn]


def get_service_turn_by_id(service_turn_id: int) -> base_api_models.ServiceTurn:
    """Get info of an existing service_turn by Id

    Args:
        service_turn_id (int): id of the service turn

    Returns:
        ServiceTurn: ServiceTurn for id
    """
    return mocks.turn


def delete_service_turn_by_id(service_turn_id: int) -> base_api_models.APIResponse:
    """Delete an existing service_turn by Id

    Args:
        service_turn_id (int): id of the service_turn

    Returns:
        APIResponse: The result of the deletion
    """
    return base_api_models.APIResponse(
        code=200, type="DELETE", message="ServiceTurn deleted successfully"
    )


def add_service_turn(
    payload: service_turn_api_models.CreateServiceTurnPayload,
) -> base_api_models.APIResponse:
    """Add a new service_turn

    Args:
        payload (CreateServiceTurnPayload): payload to create service_turn

    Returns:
        APIResponse: The result of the addition
    """
    return base_api_models.APIResponse(
        code=200, type="ADD", message="ServiceTurn added successfully"
    )


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
    return base_api_models.APIResponse(
        code=200, type="UPDATE", message="ServiceTurn updated successfully"
    )


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
    return base_api_models.APIResponse(
        code=200, type="UPDATE", message="ServiceTurn updated successfully"
    )
