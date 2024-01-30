# QMS Core API

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Testing](#testing)

## Overview

The API for the QMS Core functionality.

## Requirements

- Python 3.7+
- Install dependencies using `pip install -r requirements.txt`

## Installation

1. Clone the repository

2. Create a virtual environment
```bash
python -m venv venv
```

3. Activate the virtual environment
- On Windows:
```bash
venv\Scripts\activate
```

- On Unix or MacOS:
```
source venv/bin/activate
```

4. Install dependencies
```
pip install -r requirements.txt
```


## Environment Variables

In order to run this project, you need to set up the following environment variables. Create a `.env` file under the /app directory of your project and add the necessary values:

### `AUTH_API_BASE_URL`

- **Description:** Base url of the API for authentication.
- **Example:** 
  ```plaintext
  AUTH_API_BASE_URL=http://localhost:1234
  ```

### `APP_CLIENT_ID`

- **Description:** Client ID of the APP for authentication.
- **Example:** 
  ```plaintext
  APP_CLIENT_ID=test-client-id
  ```

### `APP_CLIENT_SECRET`

- **Description:** Client Secret of the APP for authentication.
- **Example:** 
  ```plaintext
  APP_CLIENT_SECRET=test-client-secret
  ```

### `IAM_API_KEY`

- **Description:** API key to be able to consume the IAM API
- **Example:** 
  ```plaintext
  IAM_API_KEY=test-iam-api-key
  ```

## Running the Application
Run the FastAPI application using Uvicorn:
```bash
uvicorn main:app --reload
```

### `AUTH_ALLOWED_API_KEYS`

- **Description:** A list of allowed API keys
- **Example:** 
  ```plaintext
  AUTH_ALLOWED_API_KEYS=api-key-1,api-key-w
  ```

### `AUTH_ALLOWED_IP_ADDRESSES`

- **Description:** A list of allowed IP addresses
- **Example:** 
  ```plaintext
  AUTH_ALLOWED_IP_ADDRESSES=127.0.0.1,10.0.12.13
  ```

The API will be accessible at http://localhost:5002.

## API Documentation
Swagger UI: http://127.0.0.1:5002/docs

## Testing
Run the test suite using:

```bash
pytest
```