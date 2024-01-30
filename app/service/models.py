from pydantic import BaseModel

class CreateServiceTurnPayload(BaseModel):
    customerName: str

class CreateServiceTurnResponse(BaseModel):
    id: int
    customerName: str
    ticketNumber: str
    peopleInQueue: int
