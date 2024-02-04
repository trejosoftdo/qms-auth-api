"""Customer API handlers"""

from .. import base_api_models
from . import models as customer_api_models

# pylint: disable=W0613

status = base_api_models.Status(
    id=4,
    name="Activo",
    code="ACTIVE",
    description="Estado activo.",
    type="CUSTOMER",
    isActive=True,
)


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
    return [
        base_api_models.Customer(
            id=1,
            firstName="John",
            lastName="Doe",
            email="john.doe@test.com",
            gender="M",
            yearOfBirth=1987,
            createdBy="SYSTEM",
            lastModifiedBy="SYSTEM",
            created="2023-10-20 03:14:07",
            lastModified="2023-10-20 03:14:07",
            status=status,
        )
    ]


def get_customer_by_id(customer_id: int) -> base_api_models.Customer:
    """Get info of an existing customer by Id

    Args:
        customer_id (int): id of the customer

    Returns:
        Customer: Customer for id
    """
    return base_api_models.Customer(
        id=customer_id,
        firstName="John",
        lastName="Doe",
        email="john.doe@test.com",
        gender="M",
        yearOfBirth=1987,
        createdBy="SYSTEM",
        lastModifiedBy="SYSTEM",
        created="2023-10-20 03:14:07",
        lastModified="2023-10-20 03:14:07",
        status=status,
    )


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
