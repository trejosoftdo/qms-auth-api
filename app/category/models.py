"""Category API models"""

from typing import List, Optional
from .. import base_api_models


class CreateCategoryPayload(base_api_models.CategoryBasicData):
    """Payload to create a category

    Args:
        CategoryBasicData (class): Category basic class
    """

    id: Optional[int] = None
    statusId: Optional[int] = None


class UpdateCategoryPayload(base_api_models.CategoryBasicData):
    """Payload to update a category

    Args:
        CategoryBasicData (class): Category basic class
    """

    id: Optional[int] = None
    statusId: Optional[int] = None


class PatchCategoryPayload(base_api_models.CategoryBasicData):
    """Payload to patch a category

    Args:
        CategoryBasicData (class): Category basic class
    """

    id: Optional[int] = None
    type: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    iconUrl: Optional[str] = None
    description: Optional[str] = None
    isActive: Optional[bool] = None
    statusId: Optional[int] = None


CategoryService = base_api_models.Service
CategoriesListResponse = List[base_api_models.Category]
CategoryServicesListResponse = List[CategoryService]
