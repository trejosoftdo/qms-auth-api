"""Category API mappers"""

from .. import base_api_models
from ..database import models as db_models


def map_status(status: db_models.Status) -> base_api_models.Status:
    """Maps a database status to a API status

    Args:
        status (db_models.Status): database status item

    Returns:
        base_api_models.Status: API status item
    """
    return base_api_models.Status(
        id=status.id,
        name=status.name,
        code=status.code,
        description=status.description,
        type=status.type.value,
        isActive=status.is_active,
    )


def map_category(category: db_models.Category) -> base_api_models.Category:
    """Maps a database category to a API category

    Args:
        category (db_models.Category): database category item

    Returns:
        base_api_models.Category: API category item
    """
    return base_api_models.Category(
        id=category.id,
        name=category.name,
        code=category.code,
        description=category.description,
        iconUrl=category.icon_url,
        status=map_status(category.status),
        isActive=category.is_active,
    )


def map_category_service(service: db_models.Service) -> base_api_models.Service:
    """Maps a database service to a API category service

    Args:
        service (db_models.Service): database service item

    Returns:
        base_api_models.Service: API category service item
    """
    return base_api_models.Service(
        id=service.id,
        name=service.name,
        code=service.code,
        description=service.description,
        iconUrl=service.icon_url,
        prefix=service.prefix,
        status=map_status(service.status),
        category=map_category(service.category),
        isActive=service.is_active,
    )
