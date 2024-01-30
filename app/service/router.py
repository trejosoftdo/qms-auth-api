from fastapi import APIRouter, Depends, Header
from .. import constants
from .constants import TAGS, CREATE_SERVICE_TURN_OPERATION_ID
from .. import helpers
from . import handlers
from . import models


router = APIRouter()

@router.post(
    "/{serviceId}/serviceturns",
    dependencies = [Depends(helpers.validate_token(constants.WRITE_SERVICE_TURNS_SCOPE))],
    tags = TAGS,
    operation_id = CREATE_SERVICE_TURN_OPERATION_ID,
    response_model = models.CreateServiceTurnResponse
)
def create_service_turn(
    serviceId: int,
    item: models.CreateServiceTurnPayload,
    application: str = Header(..., convert_underscores = False)
) -> models.CreateServiceTurnResponse:
    """Creates a service turn for the given service
    
    Args:
        serviceId (int): ID of service to create a turn from
        item (models.CreateServiceTurnPayload): The required payload
        application (str, optional): The application in context.
        
    Returns:
        models.CreateServiceTurnResponse: Basic information of the created service turn
    """
    return handlers.create_service_turn(application, serviceId, item)
