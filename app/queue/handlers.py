"""Queue API handlers"""

from .. import base_api_models
from . import models as queue_api_models

# pylint: disable=W0613

status = base_api_models.Status(
    id=3,
    name="Activo",
    code="ACTIVE",
    description="Estado activo.",
    type="CUSTOMER",
    isActive=True,
)

priority = base_api_models.Priority(
    id=3,
    name="Normal",
    code="NORMAL_PRIORITY",
    description="Prioridad normal",
    weight=4,
    isActive=True,
)

def get_queues(
    active: bool, offset: int, limit: int
) -> queue_api_models.QueuesListResponse:
    """Get list of queues

    Args:
        active (bool): Flag to return only active records.
        offset (int): The items to skip before collecting the result set.
        limit (int): The items to return.

    Returns:
        QueuesListResponse: List of queues
    """
    return [
        base_api_models.Queue(
            id=1,
            name="Cola 1",
            code="QUEUE_1",
            description="Primera cola",
            isActive=True,
            status=status,
            priority=priority
        )
    ]


def get_queue_by_id(queue_id: int) -> base_api_models.Queue:
    """Get info of an existing queue by Id

    Args:
        queue_id (int): id of the queue

    Returns:
        Queue: Queue for id
    """
    return base_api_models.Queue(
        id=queue_id,
        name="Cola 2",
        code="QUEUE_2",
        description="Segunda cola",
        isActive=True,
        status=status,
        priority=priority,
    )


def delete_queue_by_id(queue_id: int) -> base_api_models.APIResponse:
    """Delete an existing queue by Id

    Args:
        queue_id (int): id of the queue

    Returns:
        APIResponse: The result of the deletion
    """
    return base_api_models.APIResponse(
        code=200, type="DELETE", message="Queue deleted successfully"
    )


def add_queue(payload: queue_api_models.CreateQueuePayload) -> base_api_models.APIResponse:
    """Add a new queue

    Args:
        payload (CreateQueuePayload): payload to create queue

    Returns:
        APIResponse: The result of the addition
    """
    return base_api_models.APIResponse(
        code=200, type="ADD", message="Queue added successfully"
    )


def update_queue(
    queue_id: int, payload: queue_api_models.UpdateQueuePayload
) -> base_api_models.APIResponse:
    """Update an existing queue by Id

    Args:
        queue_id (int): id of the queue to update
        payload (UpdateQueuePayload): payload to update queue

    Returns:
        APIResponse: The result of the update
    """
    return base_api_models.APIResponse(
        code=200, type="UPDATE", message="Queue updated successfully"
    )


def partially_update_queue(
    queue_id: int, payload: queue_api_models.PatchQueuePayload
) -> base_api_models.APIResponse:
    """Partially updates an existing queue by Id

    Args:
        queue_id (int): id of the queue to partially update
        payload (PatchQueuePayload): payload to update queue

    Returns:
        APIResponse: The result of the update
    """
    return base_api_models.APIResponse(
        code=200, type="UPDATE", message="Queue updated successfully"
    )
