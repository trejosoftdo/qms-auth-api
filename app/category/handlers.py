from . import models

status = models.Status(
  id = 1,
  name = 'Out of Service',
  description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua',
  type = 'category',
  isActive = True,
)

def get_categories(
    application: str,
    active: bool,
    offset: int,
    limit: int
  ) -> models.CategoriesListResponse:
  """Get list of categories

    Args:
        application (str): The application/realm in context
        active (bool, optional): Flag to return only active records. Defaults to True.
        offset (int, optional): The number of items to skip before collecting the result set. Defaults to 0.
        limit (int, optional): The number of items to return. Defaults to 10.

    Returns:
        models.CategoriesListResponse: List of categories
    """
  return [
    models.Category(
      id = 1,
      name = 'Resultados',
      description = 'Resultados.',
      iconUrl = 'app://file-multiple',
      status = status,
      isActive = True,
    ),
    models.Category(
      id = 2,
      name = 'Analisis',
      description = 'Analisis.',
      iconUrl = 'app://poll',
      status = status,
      isActive = True,
    ),
    models.Category(
      id = 3,
      name = 'Informacion',
      description = 'Informacion.',
      iconUrl = 'app://information',
      status = status,
      isActive = True,
    ),
    models.Category(
      id = 4,
      name = 'Web',
      description = 'Web.',
      iconUrl = 'app://web',
      status = status,
      isActive = True,
    )
  ]

def get_category_services(
    application: str,
    categoryId: int,
    active: bool,
    offset: int,
    limit: int,
) -> models.CategoryServicesListResponse:
    """Gets the list of services asociated to a category for an application in context

    Args:
        application (str, optional): The application in context.
        categoryId (int): ID of category of the services to return.
        active (bool, optional): Flag to return only active records.
        offset (int, optional): The number of items to skip before collecting the result set.
        limit (int, optional): The number of items to return.
        
    Returns:
        models.CategoryServicesListResponse: The list of services for the category
    """
    category = models.Category(
      id = categoryId,
      name = 'Resultados',
      description = 'Resultados.',
      iconUrl = 'app://file-multiple',
      status = status,
      isActive = True,
    )
    return [
      models.CategoryService(
        id = 2,
        name = 'Analisis',
        description = 'Analisis.',
        iconUrl = 'app://poll',
        prefix = 'PS-NPA',
        status = status,
        category = category,
        isActive = True,
      ),
    ]