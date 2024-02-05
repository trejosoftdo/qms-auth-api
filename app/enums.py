"""Common Enums"""

from enum import Enum

class StatusType(Enum):
    """Diferent types of statuses
    """

    CATEGORY = "CATEGORY"
    SERVICE = "SERVICE"
    CUSTOMER = "CUSTOMER"
    TURN = "TURN"
    QUEUE = "QUEUE"
    APPOINTMENT = "APPOINTMENT"


class Gender(Enum):
    """Diferent types of genders
    """

    MALE = "M"
    FEMALE = "F"
    NOT_SPECIFIED = "N/S"
