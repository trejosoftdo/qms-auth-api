from fastapi import Header, Request
from .auth import api
from . import constants
from . import environment
from . import exceptions


def validate_api_access(
  request: Request,
  api_key: str = Header(..., convert_underscores = False),
):
  """Validates the access to the API

  Args:
    request (Request): incoming request
    api_key (str, optional): API Key

  Raises:
    HTTPException: Authorization error when providing an invalid api key
    HTTPException: Forbidden error when the ip addres is not an allowed one
  """
  allowed_keys = environment.allowed_api_keys.split(constants.API_KEYS_SEPARATOR) 
  allowed_adresses = environment.allowed_ip_adresses.split(constants.IP_ADDRESSES_SEPARATOR) 

  if not api_key in allowed_keys:
    raise exceptions.UNAUTHORIZED_ERROR

  if not request.client.host in allowed_adresses:
    raise exceptions.FORBIDDEN_ERROR


def validate_token(expected_scope: str):
  """Validates the authorization token checking its valididy and scopes

  Args:
      expected_scope (str): The expected scope
  """
  def _validate(
    application: str = Header(..., convert_underscores = False),
    authorization: str = Header(..., convert_underscores = False),
  ):
    """Token validation internal function

    Args:
        application (str, optional): Application id
        authorization (str, optional): Authorization token

    Raises:
        HTTPException: Internal server error when something unexpected happens.
        HTTPException: Authorization error when token is invalidd.
        HTTPException: Forbidden error when the lacking the expected scope.
    """
    is_valid = False
    is_authorized = False

    try:
      response = api.validate_token(application, authorization, expected_scope)
      data = response.json().get('data', {})
      is_valid = data.get(constants.IS_VALID_PROPERTY) == True
      is_authorized = data.get(constants.IS_AUTHORIZED_PROPERTY) == True
    except:
      raise exceptions.INTERNAL_SERVER_ERROR

    if not is_valid:
      raise exceptions.INVALID_TOKEN_ERROR

    if not is_authorized:
      raise exceptions.FORBIDDEN_ERROR

  return _validate
