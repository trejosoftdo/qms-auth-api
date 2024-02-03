"""Category API mappers"""

from . import models as api_models
from ..database import models as db_models


def map_status(status: db_models.Status) -> api_models.Status:
    """Maps a database status to a API status

    Args:
        status (db_models.Status): database status item

    Returns:
        api_models.Status: API status item
    """
    return api_models.Status(
        id=status.id,
        name=status.name,
        description=status.description,
        type=status.type.value,
        isActive=status.is_active,
    )


def map_category(category: db_models.Category) -> api_models.Category:
    """Maps a database category to a API category

    Args:
        category (db_models.Category): database category item

    Returns:
        api_models.Category: API category item
    """
    return api_models.Category(
        id=category.id,
        name=category.name,
        description=category.description,
        iconUrl=category.icon_url,
        status=map_status(category.status),
        isActive=category.is_active,
    )


def map_category_service(service: db_models.Service) -> api_models.CategoryService:
    """Maps a database service to a API category service

    Args:
        service (db_models.Service): database service item

    Returns:
        api_models.CategoryService: API category service item
    """
    return api_models.CategoryService(
        id=service.id,
        name=service.name,
        description=service.description,
        iconUrl=service.icon_url,
        prefix=service.prefix,
        status=map_status(service.status),
        category=map_category(service.category),
        isActive=service.is_active,
    )
