"""ServiceTurn API models"""

from typing import List, Optional
from .. import base_api_models


class CreateServiceTurnPayload(base_api_models.ServiceTurn):
    """Payload to create an service turn

    Args:
        ServiceTurn (class): ServiceTurn class
    """

    id: Optional[int] = None


class UpdateServiceTurnPayload(base_api_models.ServiceTurn):
    """Payload to update an service turn

    Args:
        ServiceTurn (class): ServiceTurn class
    """

    id: Optional[int] = None


class PatchServiceTurnPayload(base_api_models.ServiceTurn):
    """Payload to patch an service turn

    Args:
        ServiceTurn (class): ServiceTurn class
    """

    id: Optional[int] = None
    appointmentId: Optional[int] = None
    priorityId: Optional[int] = None
    customerId: Optional[int] = None
    statusId: Optional[int] = None
    serviceId: Optional[int] = None
    created: Optional[str] = None
    createdBy: Optional[str] = None
    lastModified: Optional[str] = None
    lastModifiedBy: Optional[str] = None


ServiceTurnsListResponse = List[base_api_models.ServiceTurn]
