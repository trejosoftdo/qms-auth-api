"""Customer API handlers"""

from .. import base_api_models
from .. import mocks
from . import models as customer_api_models

# pylint: disable=W0613


def get_customers(
    active: bool, offset: int, limit: int
) -> customer_api_models.CustomersListResponse:
    """Get list of customers

    Args:
        active (bool): Flag to return only active records.
        offset (int): The items to skip before collecting the result set.
        limit (int): The items to return.

    Returns:
        CustomersListResponse: List of customers
    """
    return [mocks.customer]


def get_customer_by_id(customer_id: int) -> base_api_models.Customer:
    """Get info of an existing customer by Id

    Args:
        customer_id (int): id of the customer

    Returns:
        Customer: Customer for id
    """
    return mocks.customer


def get_customer_serviceturns(
    customer_id: int,
) -> customer_api_models.CustomersServiceTurnsListResponse:
    """Get list of turns an existing customer by customer Id

    Args:
        customer_id (int): id of the customer

    Returns:
        CustomersServiceTurnsListResponse: List of service turns associated to customer
    """
    return [mocks.turn]


def get_customer_appointments(
    customer_id: int,
) -> customer_api_models.CustomersAppointmentsListResponse:
    """Get list of appoinments of an existing customer by customer Id

    Args:
        customer_id (int): id of the customer

    Returns:
        CustomersAppointmentsListResponse: List of appoinments associated to customer
    """
    return [mocks.appointment]


def delete_customer_by_id(customer_id: int) -> base_api_models.APIResponse:
    """Delete an existing customer by Id

    Args:
        customer_id (int): id of the customer

    Returns:
        APIResponse: The result of the deletion
    """
    return base_api_models.APIResponse(
        code=200, type="DELETE", message="Customer deleted successfully"
    )


def add_customer(
    payload: customer_api_models.CreateCustomerPayload,
) -> base_api_models.APIResponse:
    """Add a new customer

    Args:
        payload (CreateCustomerPayload): payload to create customer

    Returns:
        APIResponse: The result of the addition
    """
    return base_api_models.APIResponse(
        code=200, type="ADD", message="Customer added successfully"
    )


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
    return base_api_models.APIResponse(
        code=200, type="UPDATE", message="Customer updated successfully"
    )


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
    return base_api_models.APIResponse(
        code=200, type="UPDATE", message="Customer updated successfully"
    )
