"""Queue API models"""

from typing import List, Optional

# from pydantic import BaseModel
from .. import base_api_models


class CreateQueuePayload(base_api_models.QueueBasicData):
    """Payload to create a queue

    Args:
        Queue (class): Queue class
    """

    id: Optional[int] = None
    statusId: int
    priorityId: int


class UpdateQueuePayload(base_api_models.QueueBasicData):
    """Payload to update a queue

    Args:
        Queue (class): Queue class
    """

    id: Optional[int] = None
    statusId: int
    priorityId: int


class PatchQueuePayload(base_api_models.QueueBasicData):
    """Payload to patch a queue

    Args:
        Queue (class): Queue class
    """

    id: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    isActive: Optional[bool] = None
    statusId: Optional[int] = None
    priorityId: Optional[int] = None


QueuesListResponse = List[base_api_models.Queue]
