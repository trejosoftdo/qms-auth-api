"""Location API models"""

from typing import List, Optional
from .. import base_api_models


class CreateLocationPayload(base_api_models.Location):
    """Payload to create an location

    Args:
        Location (class): Location class
    """

    id: Optional[int] = None


class UpdateLocationPayload(base_api_models.Location):
    """Payload to update an location

    Args:
        Location (class): Location class
    """

    id: Optional[int] = None


class PatchLocationPayload(base_api_models.Location):
    """Payload to patch an location

    Args:
        Location (class): Location class
    """

    id: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    isActive: Optional[bool] = None


LocationsListResponse = List[base_api_models.Location]
