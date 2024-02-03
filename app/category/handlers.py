"""Category API handlers"""

from . import mappers
from . import models as api_models
from . import service

# pylint: disable=W0613


def get_categories(
    application: str, active: bool, offset: int, limit: int
) -> api_models.CategoriesListResponse:
    """Get list of categories

    Args:
        application (str): The application/realm in context
        active (bool, optional): Flag to return only active records. Defaults to True.
        offset (int, optional): The items to skip before collecting the result set. Defaults to 0.
        limit (int, optional): The items to return. Defaults to 10.

    Returns:
        api_models.CategoriesListResponse: List of categories
    """
    items = service.get_categories(application, active, offset, limit)
    return list(map(mappers.map_category, items))


def get_category_services(
    application: str,
    category_id: int,
    active: bool,
    offset: int,
    limit: int,
) -> api_models.CategoryServicesListResponse:
    """Gets the list of services asociated to a category for an application in context

    Args:
        application (str, optional): The application in context.
        category_id (int): ID of category of the services to return.
        active (bool, optional): Flag to return only active records.
        offset (int, optional): The number of items to skip before collecting the result set.
        limit (int, optional): The number of items to return.

    Returns:
        api_models.CategoryServicesListResponse: The list of services for the category
    """
    items = service.get_category_services(
        application,
        category_id,
        active,
        offset,
        limit,
    )
    return list(map(mappers.map_category_service, items))
