from . import models


def create_service_turn(
    application: str,
    serviceId: int,
    item: models.CreateServiceTurnPayload
) -> models.CreateServiceTurnResponse:
    """Creates a service turn for the given service
    
    Args:
        application (str, optional): The application in context.
        serviceId (int): ID of service to create a turn from
        item (models.CreateServiceTurnPayload): The required payload

    Returns:
        models.CreateServiceTurnResponse: Created service turn
    """
    return models.CreateServiceTurnResponse(
      id = 4,
      customerName = item.customerName,
      ticketNumber = 'PS-NPA-00045',
      peopleInQueue = 12
    )