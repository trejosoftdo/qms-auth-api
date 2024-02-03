"""Status API handlers"""

from . import models as api_models

# pylint: disable=W0613


def get_statuses(
    active: bool, offset: int, limit: int
) -> api_models.StatusesListResponse:
    """Get list of statuses

    Args:
        active (bool): Flag to return only active records.
        offset (int): The items to skip before collecting the result set.
        limit (int): The items to return.

    Returns:
        api_models.StatusesListResponse: List of statuses
    """
    return [
        api_models.Status(
            id=1,
            name="Activo",
            description="Estado activo",
            type="CUSTOMER",
            isActive=True,
        )
    ]


def get_status_by_id(id: int) -> api_models.Status:
    """Get info of an existing status by Id

    Args:
        id (int): id of the status

    Returns:
        api_models.Status: Status for id
    """
    return api_models.Status(
        id=id,
        name="Activo",
        description="Estado activo",
        type="CUSTOMER",
        isActive=True,
    )


def delete_status_by_id(id: int) -> api_models.APIResponse:
    """Delete an existing status by Id

    Args:
        id (int): id of the status

    Returns:
        api_models.APIResponse: The result of the deletion
    """
    return api_models.APIResponse(
        code=200, type="DELETE", message="Status deleted successfully"
    )


def add_status(payload: api_models.CreateStatusPayload) -> api_models.APIResponse:
    """Add a new status

    Args:
        payload (api_models.CreateStatusPayload): payload to create status

    Returns:
        api_models.APIResponse: The result of the addition
    """
    return api_models.APIResponse(
        code=200, type="ADD", message="Status added successfully"
    )


def update_status(
    id: int, payload: api_models.UpdateStatusPayload
) -> api_models.APIResponse:
    """Update an existing status by Id

    Args:
        id (int): id of the status to update
        payload (api_models.UpdateStatusPayload): payload to update status

    Returns:
        api_models.APIResponse: The result of the update
    """
    return api_models.APIResponse(
        code=200, type="UPDATE", message="Status updated successfully"
    )


def partially_update_status(
    id: int, payload: api_models.PatchStatusPayload
) -> api_models.APIResponse:
    """Partially updates an existing status by Id

    Args:
        id (int): id of the status to partially update
        payload (api_models.PatchStatusPayload): payload to update status

    Returns:
        api_models.APIResponse: The result of the update
    """
    return api_models.APIResponse(
        code=200, type="UPDATE", message="Status updated successfully"
    )
