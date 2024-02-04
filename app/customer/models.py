"""Customer API models"""

from typing import List, Optional

# from pydantic import BaseModel
from .. import base_api_models


class CreateCustomerPayload(base_api_models.CustomerBasicData):
    """Payload to create a customer

    Args:
        Customer (class): Customer class
    """

    id: Optional[int] = None
    statusId: int


class UpdateCustomerPayload(base_api_models.CustomerBasicData):
    """Payload to update a customer

    Args:
        Customer (class): Customer class
    """

    id: Optional[int] = None
    statusId: int


class PatchCustomerPayload(base_api_models.CustomerBasicData):
    """Payload to patch a customer

    Args:
        Customer (class): Customer class
    """

    id: Optional[int] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    gender: Optional[base_api_models.Gender] = None
    yearOfBirth: Optional[int] = None
    statusId: Optional[int] = None


CustomersListResponse = List[base_api_models.Customer]
