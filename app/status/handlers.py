"""Status API handlers"""

from .. import base_api_models
from . import models as status_api_models

# pylint: disable=W0613


def get_statuses(
    active: bool, offset: int, limit: int
) -> status_api_models.StatusesListResponse:
    """Get list of statuses

    Args:
        active (bool): Flag to return only active records.
        offset (int): The items to skip before collecting the result set.
        limit (int): The items to return.

    Returns:
        StatusesListResponse: List of statuses
    """
    return [
        base_api_models.Status(
            id=1,
            name="Activo",
            description="Estado activo",
            type="CUSTOMER",
            isActive=True,
        )
    ]


def get_status_by_id(status_id: int) -> base_api_models.Status:
    """Get info of an existing status by Id

    Args:
        status_id (int): id of the status

    Returns:
        Status: Status for id
    """
    return base_api_models.Status(
        id=status_id,
        name="Activo",
        description="Estado activo",
        type="CUSTOMER",
        isActive=True,
    )


def delete_status_by_id(status_id: int) -> base_api_models.APIResponse:
    """Delete an existing status by Id

    Args:
        status_id (int): id of the status

    Returns:
        APIResponse: The result of the deletion
    """
    return base_api_models.APIResponse(
        code=200, type="DELETE", message="Status deleted successfully"
    )


def add_status(payload: status_api_models.CreateStatusPayload) -> base_api_models.APIResponse:
    """Add a new status

    Args:
        payload (CreateStatusPayload): payload to create status

    Returns:
        APIResponse: The result of the addition
    """
    return base_api_models.APIResponse(
        code=200, type="ADD", message="Status added successfully"
    )


def update_status(
    status_id: int, payload: status_api_models.UpdateStatusPayload
) -> base_api_models.APIResponse:
    """Update an existing status by Id

    Args:
        status_id (int): id of the status to update
        payload (UpdateStatusPayload): payload to update status

    Returns:
        APIResponse: The result of the update
    """
    return base_api_models.APIResponse(
        code=200, type="UPDATE", message="Status updated successfully"
    )


def partially_update_status(
    status_id: int, payload: status_api_models.PatchStatusPayload
) -> base_api_models.APIResponse:
    """Partially updates an existing status by Id

    Args:
        status_id (int): id of the status to partially update
        payload (PatchStatusPayload): payload to update status

    Returns:
        APIResponse: The result of the update
    """
    return base_api_models.APIResponse(
        code=200, type="UPDATE", message="Status updated successfully"
    )
