"""Entry point"""

from fastapi import FastAPI
from .category import router as category
from .service import router as service
from .status import router as status
from . import constants


app = FastAPI(
    title=constants.API_TITLE,
    description=constants.API_DESCRIPTION,
    summary=constants.API_SUMMARY,
    version=constants.API_VERSION,
)

app.include_router(category.router, prefix=constants.CATEGORIES_ROUTE_PREFIX)
app.include_router(service.router, prefix=constants.SERVICES_ROUTE_PREFIX)
app.include_router(status.router, prefix=constants.STATUSES_ROUTE_PREFIX)
