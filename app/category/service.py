"""Category API service"""

from typing import List
from sqlalchemy import select
from ..database import models as db_models, main

# pylint: disable=W0613

def get_categories(
    application: str, active: bool, offset: int, limit: int
) -> List[db_models.Category]:
    """Get list of categories from database

    Args:
        application (str): The application in context
        active (bool, optional): Flag to return only active records. Defaults to True.
        offset (int, optional): The items to skip before collecting the result set. Defaults to 0.
        limit (int, optional): The items to return. Defaults to 10.

    Returns:
        List[db_models.Category]: List of categories
    """
    statement = (
        select(db_models.Category)
        .where(db_models.Category.is_active == active)
        .limit(limit)
        .offset(offset)
    )
    return main.session.scalars(statement)


def get_category_services(
    application: str,
    category_id: int,
    active: bool,
    offset: int,
    limit: int,
) -> List[db_models.Service]:
    """Gets the list of services asociated to a category for an application in context

    Args:
        application (str, optional): The application in context.
        category_id (int): ID of category of the services to return.
        active (bool, optional): Flag to return only active records.
        offset (int, optional): The number of items to skip before collecting the result set.
        limit (int, optional): The number of items to return.

    Returns:
        List[db_models.Service]: The list of services
    """
    statement = (
        select(db_models.Service)
        .where(db_models.Service.is_active == active)
        .where(db_models.Service.category_id == category_id)
        .limit(limit)
        .offset(offset)
    )
    return main.session.scalars(statement)
