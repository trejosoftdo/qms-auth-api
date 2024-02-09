"""Common Enums"""

from typing import List
from enum import Enum


class StatusType(Enum):
    """Diferent types of statuses"""

    CATEGORY = "CATEGORY"
    SERVICE = "SERVICE"
    CUSTOMER = "CUSTOMER"
    TURN = "TURN"
    QUEUE = "QUEUE"
    APPOINTMENT = "APPOINTMENT"


class Gender(Enum):
    """Diferent types of genders"""

    MALE = "M"
    FEMALE = "F"
    NOT_SPECIFIED = "N/S"

    @classmethod
    def from_val(cls, value: str) -> "Gender":
        """Gets the enum given the value

        Args:
            value (str): enum value

        Raises:
            ValueError: When the provided value does not exist within the enums

        Returns:
            Gender: Gender Enum
        """
        for v in cls.__members__.values():
            if v.value == value:
                return v

        raise ValueError(f"'{cls.__name__}' enum not found for '{value}'")

    @classmethod
    def get_values(cls) -> List[str]:
        """Gets the list of the possible enum values

        Returns:
            List[str]: List of enum values
        """
        return [v.value for v in cls.__members__.values()]
