"""Base API mappers"""

from . import base_api_models
from .database import models as db_models


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

def map_priority(priority: db_models.Priority) -> base_api_models.Priority:
    """Maps a database priority to a API priority

    Args:
        priority (db_models.Priority): database priority item

    Returns:
        base_api_models.Priority: API priority item
    """
    return base_api_models.Priority(
        id=priority.id,
        name=priority.name,
        code=priority.code,
        description=priority.description,
        weight=priority.weight,
        isActive=priority.is_active,
    )

def map_queue(queue: db_models.Queue) -> base_api_models.Queue:
    """Maps a database queue to a API queue

    Args:
        queue (db_models.Priority): database queue item

    Returns:
        base_api_models.Queue: API queue item
    """
    return base_api_models.Queue(
        id=queue.id,
        name=queue.name,
        code=queue.code,
        description=queue.description,
        isActive=queue.is_active,
        status=map_status(queue.status),
        priority=map_priority(queue.priority),
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


def map_service(service: db_models.Service) -> base_api_models.Service:
    """Maps a database service to a API service

    Args:
        service (db_models.Service): database service item

    Returns:
        base_api_models.Service: API service item
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
