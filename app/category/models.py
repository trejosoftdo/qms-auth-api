from pydantic import BaseModel
from typing import List

class Status(BaseModel):
    id: int
    name: str
    description: str
    type: str
    isActive: bool

class Category(BaseModel):
    id: int
    name: str
    description: str
    iconUrl: str
    status: Status
    isActive: bool

class CategoryService(BaseModel):
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

