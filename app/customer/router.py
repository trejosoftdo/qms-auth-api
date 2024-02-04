"""Customer API router"""

from fastapi import APIRouter, Depends
from .. import base_api_models
from .. import constants
from .. import helpers
from .constants import (
    TAGS,
    ADD_CUSTOMER_OPERATION_ID,
    DELETE_CUSTOMER_BY_ID_OPERATION_ID,
    GET_CUSTOMERS_OPERATION_ID,
    GET_CUSTOMER_BY_ID_OPERATION_ID,
    GET_CUSTOMER_APPOINTMENTS_OPERATION_ID,
    GET_CUSTOMER_SERVICE_TURNS_OPERATION_ID,
    PATCH_CUSTOMER_OPERATION_ID,
    UPDATE_CUSTOMER_OPERATION_ID,
)
from . import handlers
from . import models as customer_api_models


router = APIRouter()


@router.get(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_CUSTOMERS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_CUSTOMERS_OPERATION_ID,
    response_model=customer_api_models.CustomersListResponse,
)
def get_customers(
    active: bool = True,
    offset: int = 0,
    limit: int = 10,
) -> customer_api_models.CustomersListResponse:
    """
    Gets a list of customers
    """
    return handlers.get_customers(active, offset, limit)


@router.get(
    "/{customer_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_CUSTOMERS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_CUSTOMER_BY_ID_OPERATION_ID,
    response_model=base_api_models.Customer,
)
def get_customer_by_id(customer_id: int) -> base_api_models.Customer:
    """
    Get info of an existing customer by Id
    """
    return handlers.get_customer_by_id(customer_id)


@router.get(
    "/{customer_id}/appointments",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_CUSTOMERS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_CUSTOMER_APPOINTMENTS_OPERATION_ID,
    response_model=customer_api_models.CustomersAppointmentsListResponse,
)
def get_customer_appointments(customer_id: int) -> customer_api_models.CustomersAppointmentsListResponse:
    """
    Get list of appointments of an existing customer by customer Id
    """
    return handlers.get_customer_appointments(customer_id)

@router.get(
    "/{customer_id}/serviceturns",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_CUSTOMERS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_CUSTOMER_SERVICE_TURNS_OPERATION_ID,
    response_model=customer_api_models.CustomersServiceTurnsListResponse,
)
def get_customer_serviceturns(customer_id: int) -> customer_api_models.CustomersServiceTurnsListResponse:
    """
    Get list of turns an existing customer by customer Id
    """
    return handlers.get_customer_serviceturns(customer_id)


@router.post(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_CUSTOMERS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=ADD_CUSTOMER_OPERATION_ID,
    response_model=base_api_models.APIResponse,
)
def add_customer(
    payload: customer_api_models.CreateCustomerPayload,
) -> base_api_models.APIResponse:
    """
    Add a new customer
    """
    return handlers.add_customer(payload)


@router.put(
    "/{customer_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_CUSTOMERS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=UPDATE_CUSTOMER_OPERATION_ID,
    response_model=base_api_models.APIResponse,
)
def update_customer(
    customer_id: int, payload: customer_api_models.UpdateCustomerPayload
) -> base_api_models.APIResponse:
    """
    Update an existing customer by Id
    """
    return handlers.update_customer(customer_id, payload)


@router.patch(
    "/{customer_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_CUSTOMERS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=PATCH_CUSTOMER_OPERATION_ID,
    response_model=base_api_models.APIResponse,
)
def patch_customer(
    customer_id: int, payload: customer_api_models.PatchCustomerPayload
) -> base_api_models.APIResponse:
    """
    Update partially an existing customer by Id
    """
    return handlers.partially_update_customer(customer_id, payload)


@router.delete(
    "/{customer_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_CUSTOMERS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=DELETE_CUSTOMER_BY_ID_OPERATION_ID,
    response_model=base_api_models.APIResponse,
)
def delete_customer_by_id(customer_id: int) -> base_api_models.APIResponse:
    """
    Delete an existing customer by Id
    """
    return handlers.get_customer_by_id(customer_id)
