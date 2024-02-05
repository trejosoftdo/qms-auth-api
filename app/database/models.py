"""Database models
"""

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
from .. import enums
from . import setup

# pylint: disable=R0903
# pylint: disable=E1102


class Status(setup.Base):
    """Status related to each type of object

    Args:
        setup (Base): Database base model
    """

    __tablename__ = "statuses"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    code = Column(String(50))
    description = Column(String(500))
    type = Column(Enum(enums.StatusType))
    is_active = Column(Boolean, default=True)


class Priority(setup.Base):
    """Turn or queue priorities

    Args:
        setup (Base): Database base model
    """

    __tablename__ = "priorities"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    code = Column(String(50))
    weight = Column(Integer)
    description = Column(String(500))
    is_active = Column(Boolean, default=True)


class Category(setup.Base):
    """Categories are higher-level classification
       or grouping of customers
       or visitors based on the nature or purpose of their visit.

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
    """Services are specific assistance
       or task that a customer or visitor needs to be addressed
       at a service point (e.g., a service counter or desk).

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


class Customer(setup.Base):
    """Customers are visitors served by service agent
       or service counter

    Args:
        setup (Base): Database base model
    """

    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(200))
    gender = Column(Enum(enums.Gender))
    year_of_birth = Column(Integer)
    status_id = mapped_column(ForeignKey("statuses.id"))
    status = relationship("Status")
    created = Column(DateTime(timezone=True), server_default=func.now())
    created_by = Column(String(50))
    last_modified = Column(DateTime(timezone=True), onupdate=func.now())
    last_modified_by = Column(String(50))


class Appointment(setup.Base):
    """Appointments are pre-scheduled
       or pre-arranged time when a customer is expected
       to visit a service location to receive a specific service.

    Args:
        setup (Base): Database base model
    """

    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True)
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
    customer_id = mapped_column(ForeignKey("customers.id"))
    customer = relationship("Customer")


class ServiceTurn(setup.Base):
    """Service turns are customer's
       or visitor's time to be served by a service agent
       or at a service counter on a specific.

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
    appointment_id = mapped_column(ForeignKey("appointments.id"))
    appointment = relationship("Appointment")
    customer_id = mapped_column(ForeignKey("customers.id"))
    customer = relationship("Customer")


class Queue(setup.Base):
    """Queues are sequence of customers
       or individuals waiting for a service or assistance.

    Args:
        setup (Base): Database base model
    """

    __tablename__ = "queues"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    code = Column(String(50))
    description = Column(String(500))
    is_active = Column(Boolean, default=True)
    status_id = mapped_column(ForeignKey("statuses.id"))
    status = relationship("Status")
    priority_id = mapped_column(ForeignKey("priorities.id"))
    priority = relationship("Priority")
