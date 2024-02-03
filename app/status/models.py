"""Status API models"""

from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


class StatusType(Enum):
    """Diferent types of statuses
    """

    CATEGORY = "CATEGORY"
    SERVICE = "SERVICE"
    CUSTOMER = "CUSTOMER"
    TURN = "TURN"
    QUEUE = "QUEUE"
    APPOINTMENT = "APPOINTMENT"


class Status(BaseModel):
    """Status data

    Args:
        BaseModel (class): Base model class
    """

    id: int
    name: str
    description: str
    type: StatusType
    isActive: bool


class CreateStatusPayload(Status):
    """Payload to create an status

    Args:
        Status (class): Status class
    """

    id: Optional[int] = None


class UpdateStatusPayload(Status):
    """Payload to update an status

    Args:
        Status (class): Status class
    """

    id: Optional[int] = None


class PatchStatusPayload(Status):
    """Payload to patch an status

    Args:
        Status (class): Status class
    """

    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    isActive: Optional[bool] = None


class APIResponse(BaseModel):
    """API response

    Args:
        BaseModel (class): Base model class
    """

    code: str
    type: str
    message: str


StatusesListResponse = List[Status]
