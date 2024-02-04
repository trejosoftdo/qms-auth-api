"""Appointment API handlers"""

from .. import base_api_models
from .. import mocks
from . import models as appointment_api_models

# pylint: disable=W0613


def get_appointments(
    active: bool, offset: int, limit: int
) -> appointment_api_models.AppointmentsListResponse:
    """Get list of appointments

    Args:
        active (bool): Flag to return only active records.
        offset (int): The items to skip before collecting the result set.
        limit (int): The items to return.

    Returns:
        AppointmentsListResponse: List of appointments
    """
    return [mocks.appointment]


def get_appointment_by_id(appointment_id: int) -> base_api_models.Appointment:
    """Get info of an existing appointment by Id

    Args:
        appointment_id (int): id of the appointment

    Returns:
        Appointment: Appointment for id
    """
    return mocks.appointment


def delete_appointment_by_id(appointment_id: int) -> base_api_models.APIResponse:
    """Delete an existing appointment by Id

    Args:
        appointment_id (int): id of the appointment

    Returns:
        APIResponse: The result of the deletion
    """
    return base_api_models.APIResponse(
        code=200, type="DELETE", message="Appointment deleted successfully"
    )


def add_appointment(payload: appointment_api_models.CreateAppointmentPayload) -> base_api_models.APIResponse:
    """Add a new appointment

    Args:
        payload (CreateAppointmentPayload): payload to create appointment

    Returns:
        APIResponse: The result of the addition
    """
    return base_api_models.APIResponse(
        code=200, type="ADD", message="Appointment added successfully"
    )


def update_appointment(
    appointment_id: int, payload: appointment_api_models.UpdateAppointmentPayload
) -> base_api_models.APIResponse:
    """Update an existing appointment by Id

    Args:
        appointment_id (int): id of the appointment to update
        payload (UpdateAppointmentPayload): payload to update appointment

    Returns:
        APIResponse: The result of the update
    """
    return base_api_models.APIResponse(
        code=200, type="UPDATE", message="Appointment updated successfully"
    )


def partially_update_appointment(
    appointment_id: int, payload: appointment_api_models.PatchAppointmentPayload
) -> base_api_models.APIResponse:
    """Partially updates an existing appointment by Id

    Args:
        appointment_id (int): id of the appointment to partially update
        payload (PatchAppointmentPayload): payload to update appointment

    Returns:
        APIResponse: The result of the update
    """
    return base_api_models.APIResponse(
        code=200, type="UPDATE", message="Appointment updated successfully"
    )
