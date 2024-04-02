"""Appointment API handlers"""

from sqlalchemy.orm import Session
from .. import base_api_models
from .. import api_responses
from ..database import models as db_models
from .. import enums
from .. import mappers
from . import models as appointment_api_models


def get_appointments(
    session: Session, offset: int, limit: int
) -> appointment_api_models.AppointmentsListResponse:
    """Get list of appointments

    Args:
        session (Session): Database session
        offset (int): The items to skip before collecting the result set.
        limit (int): The items to return.

    Returns:
        AppointmentsListResponse: List of appointments
    """
    items = db_models.Appointment.find_paginated(session, limit, offset)
    return list(map(mappers.map_appointment, items))


def get_appointment_by_id(
    session: Session, appointment_id: int
) -> base_api_models.Appointment:
    """Get info of an existing appointment by Id

    Args:
        session (Session): Database session
        appointment_id (int): id of the appointment

    Returns:
        Appointment: Appointment for id
    """
    item = db_models.Appointment.find_by_id(session, appointment_id)
    return mappers.map_appointment(item)


def delete_appointment_by_id(
    session: Session, appointment_id: int
) -> base_api_models.APIResponse:
    """Delete an existing appointment by Id

    Args:
        session (Session): Database session
        appointment_id (int): id of the appointment

    Returns:
        APIResponse: The result of the deletion
    """
    db_models.Appointment.delete_by_id(session, appointment_id)
    return api_responses.ITEM_DELETED_RESPONSE


def add_appointment(
    session: Session,
    payload: appointment_api_models.CreateAppointmentPayload,
) -> base_api_models.APIResponse:
    """Add a new appointment

    Args:
        session (Session): Database session
        payload (CreateAppointmentPayload): payload to create appointment

    Returns:
        APIResponse: The result of the addition
    """
    db_models.Status.validate_status_type(
        session, payload.statusId, enums.StatusType.APPOINTMENT
    )
    db_models.Appointment.create_from_data(session, payload.dict())
    return api_responses.ITEM_ADDED_RESPONSE


def update_appointment(
    session: Session,
    appointment_id: int,
    payload: appointment_api_models.UpdateAppointmentPayload,
) -> base_api_models.APIResponse:
    """Update an existing appointment by Id

    Args:
        session (Session): Database session
        appointment_id (int): id of the appointment to update
        payload (UpdateAppointmentPayload): payload to update appointment

    Returns:
        APIResponse: The result of the update
    """
    db_models.Status.validate_status_type(
        session, payload.statusId, enums.StatusType.APPOINTMENT
    )
    db_models.Appointment.update_by_id(session, appointment_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE


def partially_update_appointment(
    session: Session,
    appointment_id: int,
    payload: appointment_api_models.PatchAppointmentPayload,
) -> base_api_models.APIResponse:
    """Partially updates an existing appointment by Id

    Args:
        session (Session): Database session
        appointment_id (int): id of the appointment to partially update
        payload (PatchAppointmentPayload): payload to update appointment

    Returns:
        APIResponse: The result of the update
    """
    if not payload.statusId is None:
        db_models.Status.validate_status_type(
            session, payload.statusId, enums.StatusType.APPOINTMENT
        )

    db_models.Appointment.update_by_id(session, appointment_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE
