"""Entry point"""

from fastapi import FastAPI
from . import constants
from .appointment import router as appointment
from .category import router as category
from .customer import router as customer
from .priority import router as priority
from .queue import router as queue
from .service import router as service
from .status import router as status


app = FastAPI(
    title=constants.API_TITLE,
    description=constants.API_DESCRIPTION,
    summary=constants.API_SUMMARY,
    version=constants.API_VERSION,
)

app.include_router(appointment.router, prefix=constants.APPOINTMENTS_ROUTE_PREFIX)
app.include_router(category.router, prefix=constants.CATEGORIES_ROUTE_PREFIX)
app.include_router(customer.router, prefix=constants.CUSTOMERS_ROUTE_PREFIX)
app.include_router(priority.router, prefix=constants.PRIORITIES_ROUTE_PREFIX)
app.include_router(queue.router, prefix=constants.QUEUES_ROUTE_PREFIX)
app.include_router(service.router, prefix=constants.SERVICES_ROUTE_PREFIX)
app.include_router(status.router, prefix=constants.STATUSES_ROUTE_PREFIX)
