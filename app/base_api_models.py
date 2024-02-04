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


class Gender(Enum):
    """Diferent types of genders
    """

    MALE = "M"
    FEMALE = "F"
    NOT_SPECIFIED = "N/S"

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


class QueueBasicData(BaseModel):
    """Queue basic data

    Args:
        BaseModel (class): Base model class
    """

    id: int
    name: str
    code: str
    description: str
    isActive: bool

class Queue(QueueBasicData):
    """Queue data

    Args:
        BaseModel (class): Base model class
    """

    status: Status
    priority: Priority


class CustomerBasicData(BaseModel):
    """Customer basic data

    Args:
        BaseModel (class): Base model class
    """

    id: int
    firstName: str
    lastName: str
    email: str
    gender: Gender
    yearOfBirth: int


class Customer(CustomerBasicData):
    """Customer data

    Args:
        BaseModel (class): Base model class
    """

    created: str
    createdBy: str
    lastModified: str
    lastModifiedBy: str
    status: Status