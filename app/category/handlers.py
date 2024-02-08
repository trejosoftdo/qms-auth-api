"""Category API handlers"""

from .. import base_api_models
from .. import api_responses
from ..database import models as db_models
from .. import mappers
from . import models as category_api_models
from . import service

# pylint: disable=W0613


def get_categories(
    application: str, active: bool, offset: int, limit: int
) -> category_api_models.CategoriesListResponse:
    """Get list of categories

    Args:
        application (str): The application/realm in context
        active (bool, optional): Flag to return only active records. Defaults to True.
        offset (int, optional): The items to skip before collecting the result set. Defaults to 0.
        limit (int, optional): The items to return. Defaults to 10.

    Returns:
        CategoriesListResponse: List of categories
    """
    items = service.get_categories(application, active, offset, limit)
    return list(map(mappers.map_category, items))


def get_category_services(
    application: str,
    category_id: int,
    active: bool,
    offset: int,
    limit: int,
) -> category_api_models.CategoryServicesListResponse:
    """Gets the list of services asociated to a category for an application in context

    Args:
        application (str, optional): The application in context.
        category_id (int): ID of category of the services to return.
        active (bool, optional): Flag to return only active records.
        offset (int, optional): The number of items to skip before collecting the result set.
        limit (int, optional): The number of items to return.

    Returns:
        CategoryServicesListResponse: The list of services for the category
    """
    items = service.get_category_services(
        application,
        category_id,
        active,
        offset,
        limit,
    )
    return list(map(mappers.map_service, items))


def get_category_by_id(category_id: int) -> base_api_models.Category:
    """Get info of an existing category by Id

    Args:
        category_id (int): id of the category

    Returns:
        Category: Category for id
    """
    item = db_models.Category.find_by_id(category_id)
    return mappers.map_category(item)


def delete_category_by_id(category_id: int) -> base_api_models.APIResponse:
    """Delete an existing category by Id

    Args:
        category_id (int): id of the category

    Returns:
        APIResponse: The result of the deletion
    """
    db_models.Category.delete_by_id(category_id)
    return api_responses.ITEM_DELETED_RESPONSE


def add_category(payload: category_api_models.CreateCategoryPayload) -> base_api_models.APIResponse:
    """Add a new category

    Args:
        payload (CreateCategoryPayload): payload to create category

    Returns:
        APIResponse: The result of the addition
    """
    db_models.Category.create_from_data(payload.dict())
    return api_responses.ITEM_ADDED_RESPONSE


def update_category(
    category_id: int, payload: category_api_models.UpdateCategoryPayload
) -> base_api_models.APIResponse:
    """Update an existing category by Id

    Args:
        category_id (int): id of the category to update
        payload (UpdateCategoryPayload): payload to update category

    Returns:
        APIResponse: The result of the update
    """
    db_models.Category.update_by_id(category_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE


def partially_update_category(
    category_id: int, payload: category_api_models.PatchCategoryPayload
) -> base_api_models.APIResponse:
    """Partially updates an existing category by Id

    Args:
        category_id (int): id of the category to partially update
        payload (PatchCategoryPayload): payload to update category

    Returns:
        APIResponse: The result of the update
    """
    db_models.Category.update_by_id(category_id, payload.dict())
    return api_responses.ITEM_UPDATED_RESPONSE
