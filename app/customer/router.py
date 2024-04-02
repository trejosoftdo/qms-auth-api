"""Customer API router"""

from fastapi import APIRouter, Depends, Query, status, Header
from sqlalchemy.orm import Session
from .. import api_responses
from .. import base_api_models
from .. import constants
from .. import helpers
from ..database import main
from .constants import (
    TAGS,
    ADD_CUSTOMER_OPERATION_ID,
    DELETE_CUSTOMER_BY_ID_OPERATION_ID,
    GET_CUSTOMERS_OPERATION_ID,
    GET_OWN_APPOINTMENTS_OPERATION_ID,
    GET_CUSTOMER_BY_ID_OPERATION_ID,
    GET_CURRENT_CUSTOMER_OPERATION_ID,
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
    responses=api_responses.responses_descriptions,
)
def get_customers(
    offset: int = Query(default=constants.DEFAULT_PAGE_OFFSET, ge=0),
    limit: int = Query(default=constants.DEFAULT_PAGE_LIMIT, ge=1),
    session: Session = Depends(main.get_session)
) -> customer_api_models.CustomersListResponse:
    """
    Gets a list of customers
    """
    return handlers.get_customers(session, offset, limit)


@router.get(
    "/current",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_OWN_CUSTOMER_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_CURRENT_CUSTOMER_OPERATION_ID,
    response_model=base_api_models.Customer,
    responses=api_responses.responses_descriptions,
)
def get_current_customer(
    application: str = Header(..., convert_underscores=False),
    authorization: str = Header(..., convert_underscores=False),
    session: Session = Depends(main.get_session)
) -> base_api_models.Customer:
    """
    Get info of of the current user customer
    """
    return handlers.get_current_customer(session, application, authorization)

@router.get(
    "/current/appointments",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_OWN_APPOINTMENTS_SCOPE)),
        Depends(helpers.validate_token(constants.READ_OWN_APPOINTMENTS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_OWN_APPOINTMENTS_OPERATION_ID,
    response_model=customer_api_models.CustomersAppointmentsResponse,
    responses=api_responses.responses_descriptions,
)
def get_own_appointments(
    application: str = Header(..., convert_underscores=False),
    authorization: str = Header(..., convert_underscores=False),
    session: Session = Depends(main.get_session)
) -> customer_api_models.CustomersAppointmentsResponse:
    """
    Get list of appointments of the current user
    """
    return handlers.get_own_appointments(session, application, authorization)


@router.get(
    "/{customer_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_CUSTOMERS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_CUSTOMER_BY_ID_OPERATION_ID,
    response_model=base_api_models.Customer,
    responses=api_responses.responses_descriptions,
)
def get_customer_by_id(
    customer_id: int,
    session: Session = Depends(main.get_session)
) -> base_api_models.Customer:
    """
    Get info of an existing customer by Id
    """
    return handlers.get_customer_by_id(session, customer_id)


@router.get(
    "/{customer_id}/appointments",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_CUSTOMERS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_CUSTOMER_APPOINTMENTS_OPERATION_ID,
    response_model=customer_api_models.Appointments,
    responses=api_responses.responses_descriptions,
)
def get_customer_appointments(
    customer_id: int,
    session: Session = Depends(main.get_session)
) -> customer_api_models.Appointments:
    """
    Get list of appointments of an existing customer by customer Id
    """
    return handlers.get_customer_appointments(session, customer_id)


@router.get(
    "/{customer_id}/serviceturns",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_CUSTOMERS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_CUSTOMER_SERVICE_TURNS_OPERATION_ID,
    response_model=customer_api_models.CustomersServiceTurnsListResponse,
    responses=api_responses.responses_descriptions,
)
def get_customer_serviceturns(
    customer_id: int,
    session: Session = Depends(main.get_session)
) -> customer_api_models.CustomersServiceTurnsListResponse:
    """
    Get list of turns an existing customer by customer Id
    """
    return handlers.get_customer_serviceturns(session, customer_id)


@router.post(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_CUSTOMERS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=ADD_CUSTOMER_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    status_code=status.HTTP_201_CREATED,
    responses=api_responses.responses_descriptions,
)
def add_customer(
    payload: customer_api_models.CreateCustomerPayload,
    session: Session = Depends(main.get_session)
) -> base_api_models.APIResponse:
    """
    Add a new customer
    """
    return handlers.add_customer(session, payload)


@router.put(
    "/{customer_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_CUSTOMERS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=UPDATE_CUSTOMER_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def update_customer(
    customer_id: int,
    payload: customer_api_models.UpdateCustomerPayload,
    session: Session = Depends(main.get_session)
) -> base_api_models.APIResponse:
    """
    Update an existing customer by Id
    """
    return handlers.update_customer(session, customer_id, payload)


@router.patch(
    "/{customer_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_CUSTOMERS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=PATCH_CUSTOMER_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def patch_customer(
    customer_id: int,
    payload: customer_api_models.PatchCustomerPayload,
    session: Session = Depends(main.get_session)
) -> base_api_models.APIResponse:
    """
    Update partially an existing customer by Id
    """
    return handlers.partially_update_customer(session, customer_id, payload)


@router.delete(
    "/{customer_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_CUSTOMERS_SCOPE)),
    ],
    tags=TAGS,
    operation_id=DELETE_CUSTOMER_BY_ID_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def delete_customer_by_id(
    customer_id: int,
    session: Session = Depends(main.get_session)
) -> base_api_models.APIResponse:
    """
    Delete an existing customer by Id
    """
    return handlers.delete_customer_by_id(session, customer_id)
