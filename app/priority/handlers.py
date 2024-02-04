"""Priority API handlers"""

from .. import base_api_models
from . import models as priority_api_models

# pylint: disable=W0613


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
    return [
        base_api_models.Priority(
            id=1,
            name="Baja",
            code="LOW_PRIORITY",
            description="Prioridad baja",
            weight=3,
            isActive=True,
        )
    ]


def get_priority_by_id(priority_id: int) -> base_api_models.Priority:
    """Get info of an existing priority by Id

    Args:
        priority_id (int): id of the priority

    Returns:
        Priority: Priority for id
    """
    return base_api_models.Priority(
        id=priority_id,
        name="Baja",
        code="LOW_PRIORITY",
        description="Prioridad baja",
        weight=3,
        isActive=True,
    )


def delete_priority_by_id(priority_id: int) -> base_api_models.APIResponse:
    """Delete an existing priority by Id

    Args:
        priority_id (int): id of the priority

    Returns:
        APIResponse: The result of the deletion
    """
    return base_api_models.APIResponse(
        code=200, type="DELETE", message="Priority deleted successfully"
    )


def add_priority(payload: priority_api_models.CreatePriorityPayload) -> base_api_models.APIResponse:
    """Add a new priority

    Args:
        payload (CreatePriorityPayload): payload to create priority

    Returns:
        APIResponse: The result of the addition
    """
    return base_api_models.APIResponse(
        code=200, type="ADD", message="Priority added successfully"
    )


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
    return base_api_models.APIResponse(
        code=200, type="UPDATE", message="Priority updated successfully"
    )


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
    return base_api_models.APIResponse(
        code=200, type="UPDATE", message="Priority updated successfully"
    )
