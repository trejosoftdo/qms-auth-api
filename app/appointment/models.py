"""Appointment API models"""

from typing import List, Optional
from .. import base_api_models


class CreateAppointmentPayload(base_api_models.Appointment):
    """Payload to create an appointment

    Args:
        Appointment (class): Appointment class
    """

    id: Optional[int] = None


class UpdateAppointmentPayload(base_api_models.Appointment):
    """Payload to update an appointment

    Args:
        Appointment (class): Appointment class
    """

    id: Optional[int] = None


class PatchAppointmentPayload(base_api_models.Appointment):
    """Payload to patch an appointment

    Args:
        Appointment (class): Appointment class
    """

    id: Optional[int] = None
    created: Optional[str] = None
    createdBy: Optional[str] = None
    lastModified: Optional[str] = None
    lastModifiedBy: Optional[str] = None
    customerId: Optional[int] = None
    statusId: Optional[int] = None
    serviceId: Optional[int] = None


AppointmentsListResponse = List[base_api_models.Appointment]
