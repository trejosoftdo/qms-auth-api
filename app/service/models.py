"""Service API models"""

from pydantic import BaseModel


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
