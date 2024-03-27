"""Customer API handlers"""

from .. import base_api_models
from .. import api_responses
from ..database import models as db_models
from ..auth import api as auth_api
from .. import enums
from .. import mappers as general_mappers
from . import models as customer_api_models


def get_customers(offset: int, limit: int) -> customer_api_models.CustomersListResponse:
    """Get list of customers

    Args:
        offset (int): The items to skip before collecting the result set.
        limit (int): The items to return.

    Returns:
        CustomersListResponse: List of customers
    """
    items = db_models.Customer.find_paginated(limit, offset)
    return list(map(general_mappers.map_customer, items))


def get_customer_by_id(customer_id: int) -> base_api_models.Customer:
    """Get info of an existing customer by Id

    Args:
        customer_id (int): id of the customer

    Returns:
        Customer: Customer for id
    """
    item = db_models.Customer.find_by_id(customer_id)
    return general_mappers.map_customer(item)


def get_current_customer(
    application: str, authorization: str
) -> base_api_models.Customer:
    """Get info of the current user

    Args:
        application (str): Application id
        authorization (str): Current user authorization


    Returns:
        Customer: Customer for id
    """
    response = auth_api.get_user_basic_data(application, authorization)
    data = response.json()
    email = data.get("data", {}).get("email", "")
    item = db_models.Customer.find_one(
        lambda x: x.where(db_models.Customer.email == email)
    )
    return general_mappers.map_customer(item)


def get_own_appointments(
    application: str, authorization: str
) -> customer_api_models.CustomersAppointmentsResponse:
    """Gets current user appointments

    Args:
        application (str): Application id
        authorization (str): Current user authorization

    Returns:
        CustomersAppointmentsResponse: List of appoinments associated to customer
    """
    customer = get_current_customer(application, authorization)
    items = db_models.Appointment.find_many(
        lambda x: x.where(db_models.Appointment.customer_id == customer.id)
    )
    print(customer)
    appointments = list(map(general_mappers.map_appointment, items))
    return customer_api_models.CustomersAppointmentsResponse(
        customer=customer,
        appointments=appointments,
    )


def get_customer_serviceturns(
    customer_id: int,
) -> customer_api_models.CustomersServiceTurnsListResponse:
    """Get list of turns an existing customer by customer Id

    Args:
        customer_id (int): id of the customer

    Returns:
        CustomersServiceTurnsListResponse: List of service turns associated to customer
    """
    items = db_models.ServiceTurn.find_many(
        lambda x: x.where(db_models.ServiceTurn.customer_id == customer_id)
    )
    return list(map(general_mappers.map_service_turn, items))


def get_customer_appointments(
    customer_id: int,
) -> customer_api_models.Appointments:
    """Get list of appoinments of an existing customer by customer Id

    Args:
        customer_id (int): id of the customer

    Returns:
        Appointments: List of appoinments associated to customer
    """
    items = db_models.Appointment.find_many(
        lambda x: x.where(db_models.Appointment.customer_id == customer_id)
    )
    return list(map(general_mappers.map_appointment, items))


def delete_customer_by_id(customer_id: int) -> base_api_models.APIResponse:
    """Delete an existing customer by Id

    Args:
        customer_id (int): id of the customer

    Returns:
        APIResponse: The result of the deletion
    """
    db_models.Customer.delete_by_id(customer_id)
    return api_responses.ITEM_DELETED_RESPONSE


def add_customer(
    payload: customer_api_models.CreateCustomerPayload,
) -> base_api_models.APIResponse:
    """Add a new customer

    Args:
        payload (CreateCustomerPayload): payload to create customer

    Returns:
        APIResponse: The result of the addition
    """
    db_models.Status.validate_status_type(payload.statusId, enums.StatusType.CUSTOMER)
    db_models.Customer.create_from_data(payload.dict())
    return api_responses.ITEM_ADDED_RESPONSE


def update_customer(
    customer_id: int, payload: customer_api_models.UpdateCustomerPayload
) -> base_api_models.APIResponse:
    """Update an existing customer by Id

    Args:
        customer_id (int): id of the customer to update
        payload (UpdateCustomerPayload): payload to update customer

    Returns:
        APIResponse: The result of the update
    """
    db_models.Status.validate_status_type(payload.statusId, enums.StatusType.CUSTOMER)
    db_models.Customer.update_by_id(customer_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE


def partially_update_customer(
    customer_id: int, payload: customer_api_models.PatchCustomerPayload
) -> base_api_models.APIResponse:
    """Partially updates an existing customer by Id

    Args:
        customer_id (int): id of the customer to partially update
        payload (PatchCustomerPayload): payload to update customer

    Returns:
        APIResponse: The result of the update
    """
    if not payload.statusId is None:
        db_models.Status.validate_status_type(
            payload.statusId, enums.StatusType.CUSTOMER
        )

    db_models.Customer.update_by_id(customer_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE
