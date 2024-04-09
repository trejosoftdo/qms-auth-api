"""Customer API handlers"""

from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import select
from .. import base_api_models
from .. import api_responses
from ..enums import StatusType
from ..database import models as db_models
from ..auth import api as auth_api
from .. import enums
from .. import mappers as general_mappers
from .. import constants
from . import models as customer_api_models


def get_status_by_code_and_type(
    session: Session, code: str, status_type: StatusType
) -> db_models.Status:
    """Gets a status by code and type

    Args:
        session (Session):  Database session
        code (str): Code of the status item
        status_type (StatusType): type of the status

    Returns:
        db_models.Status: The matched status
    """
    statement = (
        select(db_models.Status)
        .where(db_models.Status.type == status_type)
        .where(db_models.Status.code == code)
        .limit(1)
    )
    return session.scalars(statement).one()


def get_customers(
    session: Session, offset: int, limit: int
) -> customer_api_models.CustomersListResponse:
    """Get list of customers

    Args:
        session (Session): Database session
        offset (int): The items to skip before collecting the result set.
        limit (int): The items to return.

    Returns:
        CustomersListResponse: List of customers
    """
    items = db_models.Customer.find_paginated(session, limit, offset)
    return list(map(general_mappers.map_customer, items))


def get_customer_by_id(session: Session, customer_id: int) -> base_api_models.Customer:
    """Get info of an existing customer by Id

    Args:
        session (Session): Database session
        customer_id (int): id of the customer

    Returns:
        Customer: Customer for id
    """
    item = db_models.Customer.find_by_id(session, customer_id)
    return general_mappers.map_customer(item)


def get_current_customer(
    session: Session, application: str, authorization: str
) -> base_api_models.Customer:
    """Get info of the current user

    Args:
        session (Session): Database session
        application (str): Application id
        authorization (str): Current user authorization


    Returns:
        Customer: Customer for id
    """
    response = auth_api.get_user_basic_data(application, authorization)
    data = response.json()
    email = data.get("data", {}).get("email", "")
    item = db_models.Customer.find_one(
        session, lambda x: x.where(db_models.Customer.email == email)
    )
    return general_mappers.map_customer(item)


def get_own_appointments(
    session: Session, application: str, authorization: str
) -> customer_api_models.CustomersAppointmentsResponse:
    """Gets current user appointments

    Args:
        session (Session): Database session
        application (str): Application id
        authorization (str): Current user authorization

    Returns:
        CustomersAppointmentsResponse: List of appoinments associated to customer
    """
    customer = get_current_customer(session, application, authorization)
    items = db_models.Appointment.find_many(
        session, lambda x: x.where(db_models.Appointment.customer_id == customer.id)
    )
    appointments = list(map(general_mappers.map_appointment, items))
    return customer_api_models.CustomersAppointmentsResponse(
        customer=customer,
        appointments=appointments,
    )


def create_own_appointment(
    session: Session,
    payload: customer_api_models.CreateOwnAppointmentPayload,
    application: str,
    authorization: str,
) -> base_api_models.Appointment:
    """Creates a new appointment for the current user

    Args:
        session (Session): Database session
        payload (CreateOwnAppointmentPayload): Payload
        application (str): Application id
        authorization (str): Current user authorization

    Returns:
        base_api_models.Appointment: The created appointment
    """
    customer = get_current_customer(session, application, authorization)
    status = get_status_by_code_and_type(
        session, constants.DEFAULT_APPOINTMENT_STATUS, StatusType.APPOINTMENT
    )
    date = datetime.strptime(payload.date, "%Y-%m-%dT%H:%M:%S.%fZ")
    data = {
        "customerId": customer.id,
        "statusId": status.id,
        "serviceId": payload.serviceId,
        "serviceEndingExpected": date.strftime("%Y-%m-%d %H:%M:%S"),
        "lastModified": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "createdBy": customer.firstName,
        "lastModifiedBy": customer.firstName,
        # locationId: payload.locationId,
    }

    created_item = db_models.Appointment.create_from_data(session, data)
    item = db_models.Appointment.find_by_id(session, created_item.id)
    return general_mappers.map_appointment(item)


def get_customer_serviceturns(
    session: Session,
    customer_id: int,
) -> customer_api_models.CustomersServiceTurnsListResponse:
    """Get list of turns an existing customer by customer Id

    Args:
        session (Session): Database session
        customer_id (int): id of the customer

    Returns:
        CustomersServiceTurnsListResponse: List of service turns associated to customer
    """
    items = db_models.ServiceTurn.find_many(
        session, lambda x: x.where(db_models.ServiceTurn.customer_id == customer_id)
    )
    return list(map(general_mappers.map_service_turn, items))


def get_customer_appointments(
    session: Session,
    customer_id: int,
) -> customer_api_models.Appointments:
    """Get list of appoinments of an existing customer by customer Id

    Args:
        session (Session): Database session
        customer_id (int): id of the customer

    Returns:
        Appointments: List of appoinments associated to customer
    """
    items = db_models.Appointment.find_many(
        session, lambda x: x.where(db_models.Appointment.customer_id == customer_id)
    )
    return list(map(general_mappers.map_appointment, items))


def delete_customer_by_id(
    session: Session, customer_id: int
) -> base_api_models.APIResponse:
    """Delete an existing customer by Id

    Args:
        session (Session): Database session
        customer_id (int): id of the customer

    Returns:
        APIResponse: The result of the deletion
    """
    db_models.Customer.delete_by_id(session, customer_id)
    return api_responses.ITEM_DELETED_RESPONSE


def add_customer(
    session: Session,
    payload: customer_api_models.CreateCustomerPayload,
) -> base_api_models.APIResponse:
    """Add a new customer

    Args:
        session (Session): Database session
        payload (CreateCustomerPayload): payload to create customer

    Returns:
        APIResponse: The result of the addition
    """
    db_models.Status.validate_status_type(
        session, payload.statusId, enums.StatusType.CUSTOMER
    )
    db_models.Customer.create_from_data(session, payload.dict())
    return api_responses.ITEM_ADDED_RESPONSE


def update_customer(
    session: Session,
    customer_id: int,
    payload: customer_api_models.UpdateCustomerPayload,
) -> base_api_models.APIResponse:
    """Update an existing customer by Id

    Args:
        session (Session): Database session
        customer_id (int): id of the customer to update
        payload (UpdateCustomerPayload): payload to update customer

    Returns:
        APIResponse: The result of the update
    """
    db_models.Status.validate_status_type(
        session, payload.statusId, enums.StatusType.CUSTOMER
    )
    db_models.Customer.update_by_id(session, customer_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE


def partially_update_customer(
    session: Session,
    customer_id: int,
    payload: customer_api_models.PatchCustomerPayload,
) -> base_api_models.APIResponse:
    """Partially updates an existing customer by Id

    Args:
        session (Session): Database session
        customer_id (int): id of the customer to partially update
        payload (PatchCustomerPayload): payload to update customer

    Returns:
        APIResponse: The result of the update
    """
    if not payload.statusId is None:
        db_models.Status.validate_status_type(
            session, payload.statusId, enums.StatusType.CUSTOMER
        )

    db_models.Customer.update_by_id(session, customer_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE
