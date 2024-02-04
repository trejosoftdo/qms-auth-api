"""Status API models"""

from typing import List, Optional
from .. import base_api_models


class CreateStatusPayload(base_api_models.Status):
    """Payload to create an status

    Args:
        Status (class): Status class
    """

    id: Optional[int] = None


class UpdateStatusPayload(base_api_models.Status):
    """Payload to update an status

    Args:
        Status (class): Status class
    """

    id: Optional[int] = None


class PatchStatusPayload(base_api_models.Status):
    """Payload to patch an status

    Args:
        Status (class): Status class
    """

    id: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    isActive: Optional[bool] = None


StatusesListResponse = List[base_api_models.Status]
