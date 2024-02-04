"""Common API models"""

from enum import Enum
# from typing import List
from pydantic import BaseModel


class APIResponse(BaseModel):
    """API response

    Args:
        BaseModel (class): Base model class
    """

    code: str
    type: str
    message: str


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
    code: str
    description: str
    type: StatusType
    isActive: bool


class Priority(BaseModel):
    """Priority data

    Args:
        BaseModel (class): Base model class
    """

    id: int
    name: str
    code: str
    description: str
    weight: int
    isActive: bool
