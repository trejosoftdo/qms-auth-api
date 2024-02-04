"""Service API models"""

from typing import Optional, List
from pydantic import BaseModel
from .. import base_api_models


class CreateServicePayload(base_api_models.Service):
    """Payload to create a category

    Args:
        Service (class): Service class
    """

    id: Optional[int] = None


class UpdateServicePayload(base_api_models.Service):
    """Payload to update a category

    Args:
        Service (class): Service class
    """

    id: Optional[int] = None


class PatchServicePayload(base_api_models.Service):
    """Payload to patch a category

    Args:
        Service (class): Service class
    """

    id: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None
    prfix: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    isActive: Optional[bool] = None
    statusId: Optional[int] = None
    categoryId: Optional[int] = None


class CreateServiceTurnPayload(BaseModel):
    """Create Service Turn Payload data

    Args:
        BaseModel (class): Base model class
    """

    customerName: str


class CreateServiceTurnResponse(BaseModel):
    """Create Service Turn response

    Args:
        BaseModel (class): Base model class
    """

    id: int
    customerName: str
    ticketNumber: str
    peopleInQueue: int

ServicesListResponse = List[base_api_models.Service]
