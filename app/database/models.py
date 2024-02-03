"""Database models
"""

import enum
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Enum,
    Boolean,
    ForeignKey,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import mapped_column, relationship
from . import setup

# pylint: disable=R0903
# pylint: disable=E1102

class StatusType(enum.Enum):
    """Diferent types of statuses

    Args:
        enum (enum.Enum): Base enum class
    """

    CATEGORY = "CATEGORY"
    SERVICE = "SERVICE"
    CUSTOMER = "CUSTOMER"
    TURN = "TURN"
    QUEUE = "QUEUE"


class Status(setup.Base):
    """Represents the status of an entity

    Args:
        setup (Base): Database base model
    """

    __tablename__ = "statuses"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    code = Column(String(50))
    description = Column(String(500))
    type = Column(Enum(StatusType))
    is_active = Column(Boolean, default=True)


class Priority(setup.Base):
    """Represents the priority of turns

    Args:
        setup (Base): Database base model
    """

    __tablename__ = "priorities"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    code = Column(String(50))
    description = Column(String(500))
    is_active = Column(Boolean, default=True)


class Category(setup.Base):
    """Represents the category of a service

    Args:
        setup (Base): Database base model
    """

    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    code = Column(String(50))
    description = Column(String(500))
    icon_url = Column(String(1024))
    is_active = Column(Boolean, default=True)
    status_id = mapped_column(ForeignKey("statuses.id"))
    status = relationship("Status")


class Service(setup.Base):
    """Represents a service offered

    Args:
        setup (Base): Database base model
    """

    __tablename__ = "services"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    code = Column(String(50))
    prefix = Column(String(50))
    description = Column(String(500))
    icon_url = Column(String(1024))
    is_active = Column(Boolean, default=True)
    status_id = mapped_column(ForeignKey("statuses.id"))
    status = relationship("Status")
    category_id = mapped_column(ForeignKey("categories.id"))
    category = relationship("Category")


class ServiceTurn(setup.Base):
    """Represents a service turn

    Args:
        setup (Base): Database base model
    """

    __tablename__ = "service_turns"
    id = Column(Integer, primary_key=True)
    ticket_number = Column(String(30))
    customer_name = Column(String(50))
    created_by = Column(String(50))
    last_modified_by = Column(String(50))
    service_ending_expected = Column(DateTime(timezone=True))
    service_started = Column(DateTime(timezone=True))
    service_ended = Column(DateTime(timezone=True))
    created = Column(DateTime(timezone=True), server_default=func.now())
    last_modified = Column(DateTime(timezone=True), onupdate=func.now())
    status_id = mapped_column(ForeignKey("statuses.id"))
    status = relationship("Status")
    service_id = mapped_column(ForeignKey("services.id"))
    service = relationship("Service")
    priority_id = mapped_column(ForeignKey("priorities.id"))
    priority = relationship("Priority")
    # appointment_id = mapped_column(ForeignKey("appointments.id"))
    # appointment = relationship("Appointment")
    # customer_id = mapped_column(ForeignKey("customers.id"))
    # customer = relationship("Customer")
