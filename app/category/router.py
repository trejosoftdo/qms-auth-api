"""Category API router"""

from fastapi import APIRouter, Depends, Header, status
from .. import api_responses
from .. import helpers
from .. import constants
from .. import base_api_models
from .constants import (
    TAGS,
    GET_CATEGORIES_OPERATION_ID,
    GET_CATEGORY_SERVICES_OPERATION_ID,
    GET_CATEGORY_BY_ID_OPERATION_ID,
    DELETE_CATEGORY_BY_ID_OPERATION_ID,
    ADD_CATEGORY_OPERATION_ID,
    UPDATE_CATEGORY_OPERATION_ID,
    PATCH_CATEGORY_OPERATION_ID,
)
from . import handlers
from . import models as category_api_models


router = APIRouter()


@router.get(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_CATEGORIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_CATEGORIES_OPERATION_ID,
    response_model=category_api_models.CategoriesListResponse,
    responses=api_responses.responses_descriptions,
)
def get_categories(
    active: bool = True,
    offset: int = constants.DEFAULT_PAGE_OFFSET,
    limit: int = constants.DEFAULT_PAGE_LIMIT,
    application: str = Header(..., convert_underscores=False),
) -> category_api_models.CategoriesListResponse:
    """Gets a list of categories for the application in context"""
    return handlers.get_categories(application, active, offset, limit)


@router.get(
    "/{category_id}/services",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_SERVICES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_CATEGORY_SERVICES_OPERATION_ID,
    response_model=category_api_models.CategoryServicesListResponse,
    responses=api_responses.responses_descriptions,
)
def get_category_services(
    category_id: int,
    active: bool = True,
    offset: int = 0,
    limit: int = 10,
    application: str = Header(..., convert_underscores=False),
) -> category_api_models.CategoryServicesListResponse:
    """Gets the list of services asociated to a category for an application in context"""
    return handlers.get_category_services(
        application, category_id, active, offset, limit
    )


@router.get(
    "/{category_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.READ_CATEGORIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=GET_CATEGORY_BY_ID_OPERATION_ID,
    response_model=base_api_models.Category,
    responses=api_responses.responses_descriptions,
)
def get_category_by_id(category_id: int) -> base_api_models.Category:
    """
    Get info of an existing category by Id
    """
    return handlers.get_category_by_id(category_id)


@router.post(
    "/",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_CATEGORIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=ADD_CATEGORY_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    status_code=status.HTTP_201_CREATED,
)
def add_category(
    payload: category_api_models.CreateCategoryPayload,
) -> base_api_models.APIResponse:
    """
    Add a new category
    """
    return handlers.add_category(payload)


@router.put(
    "/{category_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_CATEGORIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=UPDATE_CATEGORY_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def update_category(
    category_id: int, payload: category_api_models.UpdateCategoryPayload
) -> base_api_models.APIResponse:
    """
    Update an existing category by Id
    """
    return handlers.update_category(category_id, payload)


@router.patch(
    "/{category_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_CATEGORIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=PATCH_CATEGORY_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def patch_category(
    category_id: int, payload: category_api_models.PatchCategoryPayload
) -> base_api_models.APIResponse:
    """
    Update partially an existing category by Id
    """
    return handlers.partially_update_category(category_id, payload)


@router.delete(
    "/{category_id}",
    dependencies=[
        Depends(helpers.validate_api_access),
        Depends(helpers.validate_token(constants.WRITE_CATEGORIES_SCOPE)),
    ],
    tags=TAGS,
    operation_id=DELETE_CATEGORY_BY_ID_OPERATION_ID,
    response_model=base_api_models.APIResponse,
    responses=api_responses.responses_descriptions,
)
def delete_category_by_id(category_id: int) -> base_api_models.APIResponse:
    """
    Delete an existing category by Id
    """
    return handlers.delete_category_by_id(category_id)
