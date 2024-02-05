"""General constants"""

BEARER_PORTION = "Bearer "
IS_AUTHORIZED_PROPERTY = "isAuthorized"
IS_VALID_PROPERTY = "isValid"
SCOPE_PROPERTY = "scope"
SCOPES_SEPARATOR = " "
API_KEYS_SEPARATOR = ","
IP_ADDRESSES_SEPARATOR = ","
EMPTY_VALUE = ""
TIMEOUT = 10
SYSTEM_CREATOR = "SYSTEM"
DEFAULT_TURN_STATUS = "PENDING"
DEFAULT_TURN_PRIORITY = "NORMAL_PRIORITY"

# Scopes START

# Read status information
READ_STATUSES_SCOPE="read_statuses"
# Create, modify and delete status information
WRITE_STATUSES_SCOPE="write_statuses"
# Administrate status information
ADMIN_STATUSES_SCOPE="admin_statuses"

# Read priority information
READ_PRIORITIES_SCOPE="read_priorities"
# Create, modify and delete priority information
WRITE_PRIORITIES_SCOPE="write_priorities"
# Administrate priority information
ADMIN_PRIORITIES_SCOPE="admin_priorities"

# Read category information
READ_CATEGORIES_SCOPE = "read_categories"
# Create, modify and delete category information
WRITE_CATEGORIES_SCOPE = "write_categories"
# Administrate category information
ADMIN_CATEGORIES_SCOPE = "admin_categories"

# Read service information
READ_SERVICES_SCOPE = "read_services"
# Create, modify and delete service information
WRITE_SERVICES_SCOPE = "write_services"
# Administrate service information
ADMIN_SERVICES_SCOPE = "admin_services"

# Read services turns information
READ_SERVICE_TURNS_SCOPE = "read_serviceturns"
# Create, modify and delete services turns information
WRITE_SERVICE_TURNS_SCOPE = "write_serviceturns"
# Administrate services turns information
ADMIN_SERVICE_TURNS_SCOPE = "admin_serviceturns"

# Read customer information
READ_CUSTOMERS_SCOPE = "read_customers"
# Create, modify and delete customer information
WRITE_CUSTOMERS_SCOPE = "write_customers"
# Administrate customer information
ADMIN_CUSTOMERS_SCOPE = "admin_customers"

# Read customers' appointments information
READ_APPOINTMENTS_SCOPE = "read_appointments"
# Create, modify and delete customers' appointments information
WRITE_APPOINTMENTS_SCOPE = "write_appointments"
# Administrate customers' appointments information
ADMIN_APPOINTMENTS_SCOPE = "admin_appointments"

# Read queue information
READ_QUEUES_SCOPE = "read_queues"
# Create, modify and delete queue information
WRITE_QUEUES_SCOPE = "write_queues"
# Administrate queue
ADMIN_QUEUES_SCOPE = "admin_queues"

# Scopes END

# API Metadata
API_TITLE = "QMS Core API"
API_SUMMARY = "API for QMS Core functionality."
API_DESCRIPTION = "The API for the QMS Core functionality."
API_VERSION = "1.0.0"

# API routes prefixes
APPOINTMENTS_ROUTE_PREFIX = "/api/v1/appointments"
CATEGORIES_ROUTE_PREFIX = "/api/v1/categories"
CUSTOMERS_ROUTE_PREFIX = "/api/v1/customers"
PRIORITIES_ROUTE_PREFIX = "/api/v1/priorities"
QUEUES_ROUTE_PREFIX = "/api/v1/queues"
SERVICES_ROUTE_PREFIX = "/api/v1/services"
SERVICE_TURNS_ROUTE_PREFIX = "/api/v1/serviceturns"
STATUSES_ROUTE_PREFIX = "/api/v1/statuses"

# Environment names
AUTH_API_BASE_URL_ENV_NAME = "AUTH_API_BASE_URL"
APP_CLIENT_ID_ENV_NAME = "APP_CLIENT_ID"
APP_CLIENT_SECRET_ENV_NAME = "APP_CLIENT_SECRET"
IAM_API_KEY_ENV_NAME = "IAM_API_KEY"
AUTH_ALLOWED_IP_ADDRESSES_ENV_NAME = "AUTH_ALLOWED_IP_ADDRESSES"
AUTH_ALLOWED_API_KEYS_ENV_NAME = "AUTH_ALLOWED_API_KEYS"
DB_CONNECTION_STRING_ENV_NAME = "DB_CONNECTION_STRING"

# Errors
INTERNAL_SERVER_ERROR_MESSAGE = "Internal Server Error"
INTERNAL_SERVER_ERROR_CODE = 500

INVALID_TOKEN_ERROR_MESSAGE = "Invalid token"
INVALID_TOKEN_ERROR_CODE = 401

FORBIDDEN_ERROR_MESSAGE = "Forbidden"
FORBIDDEN_ERROR_CODE = 403

UNAUTHORIZED_ERROR_MESSAGE = "Unauthorized"
UNAUTHORIZED_ERROR_CODE = 401
