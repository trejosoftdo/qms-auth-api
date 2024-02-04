"""Priority API models"""

from typing import List, Optional

# from pydantic import BaseModel
from .. import base_api_models


class CreatePriorityPayload(base_api_models.Priority):
    """Payload to create an priority

    Args:
        Priority (class): Priority class
    """

    id: Optional[int] = None


class UpdatePriorityPayload(base_api_models.Priority):
    """Payload to update an priority

    Args:
        Priority (class): Priority class
    """

    id: Optional[int] = None


class PatchPriorityPayload(base_api_models.Priority):
    """Payload to patch an priority

    Args:
        Priority (class): Priority class
    """

    id: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    weight: Optional[int] = None
    isActive: Optional[bool] = None


PrioritiesListResponse = List[base_api_models.Priority]
