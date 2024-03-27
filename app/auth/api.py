"""Auth API"""

import requests
from .. import environment
from .. import constants


common_headers = {
    "Content-Type": "application/json",
    "api_key": environment.iam_api_key,
}

common_payload = {
    "clientId": environment.app_client_id,
    "clientSecret": environment.app_client_secret,
}


def validate_token(
    application: str, authorization: str, expected_scope: str
) -> requests.Response:
    """Gets information such as scope and active from the given token

    Args:
        application (str): The application in context
        authorization (str): The access token to validate
        expected_scope (str): The expected scope

    Returns:
        requests.Response: The response from the auth API.
    """
    url = f"{environment.auth_api_base_url}/api/v1/auth/token/validate"
    payload = {
        **common_payload,
        "expectedScope": expected_scope,
    }
    headers = {
        **common_headers,
        "application": application,
        "authorization": authorization,
    }
    return requests.post(url, headers=headers, json=payload, timeout=constants.TIMEOUT)


def get_user_basic_data(application: str, authorization: str) -> requests.Response:
    """Gets the user basic for the authorization

    Args:
        application (str): The application in context
        authorization (str): The access token of the user

    Returns:
        requests.Response: The response from the auth API.
    """
    url = f"{environment.auth_api_base_url}/api/v1/auth/user-basic-data"
    payload = {
        **common_payload,
    }
    headers = {
        **common_headers,
        "application": application,
        "authorization": authorization,
    }
    return requests.post(url, headers=headers, json=payload, timeout=constants.TIMEOUT)
