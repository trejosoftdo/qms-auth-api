"""Service API mappers"""

from . import models as api_models
from ..database import models as db_models


def map_service_turn_response(
    turn: db_models.ServiceTurn,
) -> api_models.CreateServiceTurnResponse:
    """Maps a database service turn to a API Service Turn Response

    Args:
        turn (db_models.ServiceTurn): database service turn

    Returns:
        api_models.CreateServiceTurnResponse: API Service Turn Response
    """
    return api_models.CreateServiceTurnResponse(
        id=turn.id,
        customerName=turn.customer_name,
        ticketNumber=turn.ticket_number,
        peopleInQueue=12,
    )
