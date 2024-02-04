from . import base_api_models


status = base_api_models.Status(
    id=4,
    name="Activo",
    code="ACTIVE",
    description="Estado activo.",
    type="CUSTOMER",
    isActive=True,
)

priority = base_api_models.Priority(
    id=1,
    name="Baja",
    code="LOW_PRIORITY",
    description="Prioridad baja",
    weight=3,
    isActive=True,
)

queue = base_api_models.Queue(
    id=1,
    name="Cola 1",
    code="QUEUE_1",
    description="Primera cola",
    isActive=True,
    status=status,
    priority=priority
)

category = base_api_models.Category(
    id=1,
    name="Categoria 1",
    code="CATEGORY_1",
    description="Primera categoria",
    iconUrl="app://foo",
    isActive=True,
    status=status,
)

service = base_api_models.Service(
    id=1,
    name="Categoria 1",
    code="CATEGORY_1",
    description="Primera categoria",
    iconUrl="app://foo",
    isActive=True,
    status=status,
    category=category,
    prefix="FOO-BAR-1234",
)

customer = base_api_models.Customer(
    id=1,
    firstName="John",
    lastName="Doe",
    email="john.doe@test.com",
    gender="M",
    yearOfBirth=1987,
    createdBy="SYSTEM",
    lastModifiedBy="SYSTEM",
    created="2023-10-20 03:14:07",
    lastModified="2023-10-20 03:14:07",
    status=status,
)

appointment = base_api_models.Appointment(
    id=1,
    createdBy="SYSTEM",
    lastModifiedBy="SYSTEM",
    created="2023-10-20 03:14:07",
    lastModified="2023-10-20 03:14:07",
    serviceStarted="2023-10-20 03:14:07",
    serviceEndingExpected="2023-10-20 03:14:07",
    serviceEnded="2023-10-20 03:14:07",
    status=status,
    customer=customer,
    service=service,
)


turn = base_api_models.ServiceTurn(
    id=1,
    createdBy="SYSTEM",
    lastModifiedBy="SYSTEM",
    created="2023-10-20 03:14:07",
    lastModified="2023-10-20 03:14:07",
    serviceStarted="2023-10-20 03:14:07",
    serviceEndingExpected="2023-10-20 03:14:07",
    serviceEnded="2023-10-20 03:14:07",
    ticketNumber="PA-FOO-1234",
    customerName="John Doe",
    status=status,
    priority=priority,
    customer=customer,
    appointment=appointment,
    service=service,
)