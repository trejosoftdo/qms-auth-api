from dotenv import load_dotenv
import os
from . import constants

load_dotenv()

auth_api_base_url = os.getenv(constants.AUTH_API_BASE_URL_ENV_NAME)
app_client_id = os.getenv(constants.APP_CLIENT_ID_ENV_NAME)
app_client_secret = os.getenv(constants.APP_CLIENT_SECRET_ENV_NAME)
iam_api_key = os.getenv(constants.IAM_API_KEY_ENV_NAME)