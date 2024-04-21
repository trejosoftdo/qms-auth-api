"""Base API mappers"""

from . import base_api_models
from .database import models as db_models
from .enums import Gender
from .constants import NOT_AVAILABLE


def map_status(status: db_models.Status) -> base_api_models.Status:
    """Maps a database status to a API status

    Args:
        status (db_models.Status): database status item

    Returns:
        base_api_models.Status: API status item
    """
    return base_api_models.Status(
        id=status.id,
        name=status.name,
        code=status.code,
        description=status.description,
        type=status.type.value,
        isActive=status.is_active,
    )


def map_priority(priority: db_models.Priority) -> base_api_models.Priority:
    """Maps a database priority to a API priority

    Args:
        priority (db_models.Priority): database priority item

    Returns:
        base_api_models.Priority: API priority item
    """
    return base_api_models.Priority(
        id=priority.id,
        name=priority.name,
        code=priority.code,
        description=priority.description,
        weight=priority.weight,
        isActive=priority.is_active,
    )

def map_location(location: db_models.Location) -> base_api_models.Location:
    """Maps a database location to a API location

    Args:
        location (db_models.Location): database location item

    Returns:
        base_api_models.Location: API location item
    """
    return base_api_models.Location(
        id=location.id,
        name=location.name,
        code=location.code,
        description=location.description,
        address=location.address,
        isActive=location.is_active,
    )


def map_queue(queue: db_models.Queue) -> base_api_models.Queue:
    """Maps a database queue to a API queue

    Args:
        queue (db_models.Priority): database queue item

    Returns:
        base_api_models.Queue: API queue item
    """
    return base_api_models.Queue(
        id=queue.id,
        name=queue.name,
        code=queue.code,
        description=queue.description,
        isActive=queue.is_active,
        status=map_status(queue.status),
        priority=map_priority(queue.priority),
    )


def map_category(category: db_models.Category) -> base_api_models.Category:
    """Maps a database category to a API category

    Args:
        category (db_models.Category): database category item

    Returns:
        base_api_models.Category: API category item
    """
    return base_api_models.Category(
        id=category.id,
        name=category.name,
        code=category.code,
        description=category.description,
        iconUrl=category.icon_url,
        status=map_status(category.status),
        isActive=category.is_active,
    )


def map_service(service: db_models.Service) -> base_api_models.Service:
    """Maps a database service to a API service

    Args:
        service (db_models.Service): database service item

    Returns:
        base_api_models.Service: API service item
    """
    return base_api_models.Service(
        id=service.id,
        name=service.name,
        code=service.code,
        description=service.description,
        iconUrl=service.icon_url,
        prefix=service.prefix,
        status=map_status(service.status),
        category=map_category(service.category),
        isActive=service.is_active,
    )


def map_customer(customer: db_models.Customer) -> base_api_models.Customer:
    """Maps a database customer to a API customer

    Args:
        customer (db_models.Customer): database customer item

    Returns:
        base_api_models.Customer: API customer item
    """
    return base_api_models.Customer(
        id=customer.id,
        firstName=customer.first_name,
        lastName=customer.last_name,
        email=customer.email,
        gender=Gender.from_val(customer.gender),
        yearOfBirth=customer.year_of_birth,
        created=str(customer.created),
        createdBy=customer.created_by or NOT_AVAILABLE,
        lastModified=str(customer.last_modified),
        lastModifiedBy=customer.last_modified_by or NOT_AVAILABLE,
        status=map_status(customer.status),
    )


def map_appointment(appointment: db_models.Appointment) -> base_api_models.Appointment:
    """Maps a database appointment to a API appointment

    Args:
        appointment (db_models.Appointment): database appointment item

    Returns:
        base_api_models.Appointment: API appointment item
    """
    return base_api_models.Appointment(
        id=appointment.id,
        createdBy=appointment.created_by or NOT_AVAILABLE,
        lastModifiedBy=appointment.last_modified_by or NOT_AVAILABLE,
        serviceEndingExpected=str(appointment.service_ending_expected),
        serviceStarted=str(appointment.service_started),
        serviceEnded=str(appointment.service_ended),
        created=str(appointment.created),
        lastModified=str(appointment.last_modified),
        status=map_status(appointment.status),
        service=map_service(appointment.service),
        customer=map_customer(appointment.customer),
    )


def map_service_turn(turn: db_models.ServiceTurn) -> base_api_models.ServiceTurn:
    """Maps a database service turn to a API service turn

    Args:
        turn (db_models.ServiceTurn): database service turn item

    Returns:
        base_api_models.ServiceTurn: API service turn item
    """
    return base_api_models.ServiceTurn(
        id=turn.id,
        ticketNumber=turn.ticket_number,
        customerName=turn.customer_name,
        createdBy=turn.created_by or NOT_AVAILABLE,
        lastModifiedBy=turn.last_modified_by or NOT_AVAILABLE,
        serviceEndingExpected=str(turn.service_ending_expected),
        serviceStarted=str(turn.service_started),
        serviceEnded=str(turn.service_ended),
        created=str(turn.created),
        lastModified=str(turn.last_modified),
        priority=map_priority(turn.priority),
        appointment=map_appointment(turn.appointment) if not turn.appointment is None else None,
        status=map_status(turn.status),
        service=map_service(turn.service),
        customer=map_customer(turn.customer) if not turn.customer is None else None,
    )


def map_turn_status_item(turn: db_models.ServiceTurn) -> base_api_models.ServiceTurnStatusItem:
    """Maps a service turn status item from the given data

    Args:
        turn (db_models.ServiceTurn): database service turn item

    Returns:
        base_api_models.ServiceTurnStatusItem: Service Turn status item
    """
    return base_api_models.ServiceTurnStatusItem(
        ticketNumber=turn.ticket_number,
        queueName=turn.service.name,
        statusName=turn.status.name,
        statusCode=turn.status.code,
    )
