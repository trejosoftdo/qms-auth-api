"""Category API models"""

from typing import List
from pydantic import BaseModel


class Status(BaseModel):
    """Status data

    Args:
        BaseModel (class): Base model class
    """

    id: int
    name: str
    description: str
    type: str
    isActive: bool


class Category(BaseModel):
    """Category data

    Args:
        BaseModel (class): Base model class
    """

    id: int
    name: str
    description: str
    iconUrl: str
    status: Status
    isActive: bool


class CategoryService(BaseModel):
    """Category Service data

    Args:
        BaseModel (class): Base model class
    """

    id: int
    name: str
    description: str
    prefix: str
    iconUrl: str
    status: Status
    category: Category
    isActive: bool


CategoriesListResponse = List[Category]
CategoryServicesListResponse = List[CategoryService]
