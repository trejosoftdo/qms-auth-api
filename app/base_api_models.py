"""Common API models"""

from typing import Optional
from pydantic import BaseModel
from . import enums


class APIResponse(BaseModel):
    """API response

    Args:
        BaseModel (class): Base model class
    """

    code: str
    type: str
    message: str


class Status(BaseModel):
    """Status data

    Args:
        BaseModel (class): Base model class
    """

    id: int
    name: str
    code: str
    description: str
    type: enums.StatusType
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


class Location(BaseModel):
    """Location data

    Args:
        BaseModel (class): Base model class
    """

    id: int
    name: str
    code: str
    description: str
    address: str
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


class CategoryBasicData(BaseModel):
    """Category basic data

    Args:
        BaseModel (class): Base model class
    """

    id: int
    name: str
    code: str
    description: str
    iconUrl: str
    isActive: bool


class Category(CategoryBasicData):
    """Category data

    Args:
        BaseModel (class): Base model class
    """

    status: Status


class ServiceBasicData(BaseModel):
    """Service basic data

    Args:
        BaseModel (class): Base model class
    """

    id: int
    name: str
    description: str
    prefix: str
    iconUrl: str
    isActive: bool


class Service(ServiceBasicData):
    """Service data

    Args:
        BaseModel (class): Base model class
    """

    category: Category
    status: Status


class CustomerBasicData(BaseModel):
    """Customer basic data

    Args:
        BaseModel (class): Base model class
    """

    id: int
    firstName: str
    lastName: str
    email: str
    gender: enums.Gender
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


class AppointmentBasicData(BaseModel):
    """Appointment basic data

    Args:
        BaseModel (class): Base model class
    """

    id: int


class Appointment(AppointmentBasicData):
    """Appointment data

    Args:
        BaseModel (class): Base model class
    """

    created: str
    createdBy: str
    lastModified: str
    lastModifiedBy: str
    serviceStarted: Optional[str] = None
    serviceEndingExpected: Optional[str] = None
    serviceEnded: Optional[str] = None
    customer: Customer
    status: Status
    service: Service
    location: Location


class ServiceTurnBasicData(BaseModel):
    """Service turn basic data

    Args:
        BaseModel (class): Base model class
    """

    id: int
    ticketNumber: str
    customerName: Optional[str] = None


class ServiceTurn(ServiceTurnBasicData):
    """Service turn data

    Args:
        BaseModel (class): Base model class
    """

    created: str
    createdBy: str
    lastModified: str
    lastModifiedBy: str
    serviceStarted: Optional[str] = None
    serviceEndingExpected: Optional[str] = None
    serviceEnded: Optional[str] = None
    priority: Priority
    status: Status
    service: Service
    appointment: Optional[Appointment] = None
    customer: Optional[Customer] = None

class ServiceTurnStatusItem(BaseModel):
    """Service Turn Status Item data

    Args:
        BaseModel (class): Base model class
    """

    ticketNumber: str
    queueName: str
    statusName: str
    statusCode: str
