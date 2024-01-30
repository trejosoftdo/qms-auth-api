BEARER_PORTION = 'Bearer '
IS_AUTHORIZED_PROPERTY = 'isAuthorized'
IS_VALID_PROPERTY = 'isValid'
SCOPE_PROPERTY = 'scope'
SCOPES_SEPARATOR = ' '
API_KEYS_SEPARATOR = ','
IP_ADDRESSES_SEPARATOR = ','
EMPTY_VALUE = ''


# Device Token Auth
READ_CATEGORIES_SCOPE = 'read_categories'
READ_SERVICES_SCOPE = 'read_services'
READ_SERVICE_TURNS_SCOPE = 'read_serviceturns'
WRITE_SERVICE_TURNS_SCOPE = 'write_serviceturns'

DEVICE_TOKEN_SCOPES = (
  READ_CATEGORIES_SCOPE,
  READ_SERVICES_SCOPE,
  READ_SERVICE_TURNS_SCOPE,
  WRITE_SERVICE_TURNS_SCOPE
)

# API Metadata
API_TITLE = 'QMS Core API'
API_SUMMARY = 'API for QMS Core functionality.'
API_DESCRIPTION = 'The API for the QMS Core functionality.'
API_VERSION =  '1.0.0'

# API routes prefixes
CATEGORIES_ROUTE_PREFIX = '/api/v1/categories'
SERVICES_ROUTE_PREFIX = '/api/v1/services'

# Environment names
AUTH_API_BASE_URL_ENV_NAME = 'AUTH_API_BASE_URL'
APP_CLIENT_ID_ENV_NAME = 'APP_CLIENT_ID'
APP_CLIENT_SECRET_ENV_NAME = 'APP_CLIENT_SECRET'
IAM_API_KEY_ENV_NAME = 'IAM_API_KEY'
AUTH_ALLOWED_IP_ADDRESSES_ENV_NAME = 'AUTH_ALLOWED_IP_ADDRESSES'
AUTH_ALLOWED_API_KEYS_ENV_NAME = 'AUTH_ALLOWED_API_KEYS'

# Errors
INTERNAL_SERVER_ERROR_MESSAGE = 'Internal Server Error'
INTERNAL_SERVER_ERROR_CODE = 500

INVALID_TOKEN_ERROR_MESSAGE = 'Invalid token'
INVALID_TOKEN_ERROR_CODE = 401

FORBIDDEN_ERROR_MESSAGE = 'Forbidden'
FORBIDDEN_ERROR_CODE = 403

UNAUTHORIZED_ERROR_MESSAGE = 'Unauthorized'
UNAUTHORIZED_ERROR_CODE = 401
