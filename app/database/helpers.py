"""Database helpers
"""

from typing import Callable
import re
from sqlalchemy.exc import IntegrityError
from app import constants, exceptions
from . import main


def is_a_duplicate_exception(exc: Exception) -> bool:
    """Checks if a thrown exception was due to a duplicate found

    Args:
        exc (Exception): The thrown exception

    Returns:
        bool: True if the exception was due to a duplicate found
              otherwise False
    """
    return constants.DUPLICATE_KEYWORD in str(exc)


def to_snake_case(text: str) -> str:
    """Changes from camel case to snake case

    Args:
        text (str): text in camel case

    Returns:
        str: text in snake case
    """
    return re.sub(
        r"(?<=[a-z0-9])[A-Z]+|(?<=[A-Za-z])[0-9]", lambda m: f"_{m[0].lower()}", text
    )


def snake_case_props(data: dict) -> dict:
    """Tranform the properties of the data to snake case

    Args:
        data (dict): source data

    Returns:
        dict: resulting data
    """
    return {to_snake_case(name): data[name] for name in data}


def handle_session_rollback(func: Callable):
    """Rollbacks the current session when an exception occurrs

    Args:
        func (Callable): Wrapped Function
    """

    def handled(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            print(args[0])
            # main.session.rollback()
            raise

    return handled


def handle_duplicate_error(func: Callable):
    """Handles database duplicate error

    Args:
        func (Callable): Wrapped Function
    """

    def handled(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IntegrityError as exc:
            if is_a_duplicate_exception(exc):
                raise exceptions.CONFLICT_ERROR from exc
            raise exc

    return handled
