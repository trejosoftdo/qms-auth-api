"""Service API handlers"""

from . import models
from . import mappers
from . import service

# pylint: disable=W0613

def create_service_turn(
    application: str, service_id: int, item: models.CreateServiceTurnPayload
) -> models.CreateServiceTurnResponse:
    """Creates a service turn for the given service

    Args:
        application (str, optional): The application in context.
        service_id (int): ID of service to create a turn from
        item (models.CreateServiceTurnPayload): The required payload

    Returns:
        models.CreateServiceTurnResponse: Created service turn
    """
    item = service.create_service_turn(
        application,
        service_id,
        item,
    )
    return mappers.map_service_turn_response(item)
