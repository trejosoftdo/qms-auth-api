"""Queue API handlers"""

from sqlalchemy.orm import Session
from .. import base_api_models
from .. import api_responses
from ..database import models as db_models
from .. import enums
from .. import mappers
from . import models as queue_api_models


def get_queues(
    session: Session, active: bool, offset: int, limit: int
) -> queue_api_models.QueuesListResponse:
    """Get list of queues

    Args:
        session (Session): Database session
        active (bool): Flag to return only active records.
        offset (int): The items to skip before collecting the result set.
        limit (int): The items to return.

    Returns:
        QueuesListResponse: List of queues
    """
    items = db_models.Queue.find_paginated(
        session, limit, offset, lambda x: x.where(db_models.Queue.is_active == active)
    )
    return list(map(mappers.map_queue, items))


def get_queue_by_id(session: Session, queue_id: int) -> base_api_models.Queue:
    """Get info of an existing queue by Id

    Args:
        session (Session): Database session
        queue_id (int): id of the queue

    Returns:
        Queue: Queue for id
    """
    item = db_models.Queue.find_by_id(session, queue_id)
    return mappers.map_queue(item)


def delete_queue_by_id(session: Session, queue_id: int) -> base_api_models.APIResponse:
    """Delete an existing queue by Id

    Args:
        session (Session): Database session
        queue_id (int): id of the queue

    Returns:
        APIResponse: The result of the deletion
    """
    db_models.Queue.delete_by_id(session, queue_id)
    return api_responses.ITEM_DELETED_RESPONSE


def add_queue(
    session: Session, payload: queue_api_models.CreateQueuePayload
) -> base_api_models.APIResponse:
    """Add a new queue

    Args:
        session (Session): Database session
        payload (CreateQueuePayload): payload to create queue

    Returns:
        APIResponse: The result of the addition
    """
    db_models.Status.validate_status_type(
        session, payload.statusId, enums.StatusType.QUEUE
    )
    db_models.Queue.create_from_data(session, payload.dict())
    return api_responses.ITEM_ADDED_RESPONSE


def update_queue(
    session: Session, queue_id: int, payload: queue_api_models.UpdateQueuePayload
) -> base_api_models.APIResponse:
    """Update an existing queue by Id

    Args:
        session (Session): Database session
        queue_id (int): id of the queue to update
        payload (UpdateQueuePayload): payload to update queue

    Returns:
        APIResponse: The result of the update
    """
    db_models.Status.validate_status_type(
        session, payload.statusId, enums.StatusType.QUEUE
    )
    db_models.Queue.update_by_id(session, queue_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE


def partially_update_queue(
    session: Session, queue_id: int, payload: queue_api_models.PatchQueuePayload
) -> base_api_models.APIResponse:
    """Partially updates an existing queue by Id

    Args:
        session (Session): Database session
        queue_id (int): id of the queue to partially update
        payload (PatchQueuePayload): payload to update queue

    Returns:
        APIResponse: The result of the update
    """
    if not payload.statusId is None:
        db_models.Status.validate_status_type(
            session, payload.statusId, enums.StatusType.QUEUE
        )

    db_models.Queue.update_by_id(session, queue_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE
