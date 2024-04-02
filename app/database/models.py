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
    UniqueConstraint,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import mapped_column, relationship, Session
from app import enums, exceptions
from . import setup
from .mixins import ModelMethodsMixin


# pylint: disable=R0903
# pylint: disable=E1102


class Status(ModelMethodsMixin, setup.Base):
    """Status related to each type of object"""

    __tablename__ = "statuses"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    code = Column(String(50))
    description = Column(String(500))
    type = Column(Enum(enums.StatusType))
    is_active = Column(Boolean, default=True)
    __table_args__ = (
        UniqueConstraint("name", "type", name="status_name_and_type_unique"),
        UniqueConstraint("code", "type", name="status_code_and_type_unique"),
    )


    @classmethod
    def validate_status_type(
        cls: "Status",
        session: Session,
        status_id: int,
        status_type: enums.StatusType
    ):
        """Checks if a status is of a type

        Args:
            session (Session): Database session
            status_id (int): ID of status
            status_type (StatusType): expected type of the status
        """
        item = cls.find_by_id(session, status_id)

        if item.type != status_type:
            raise exceptions.INVALID_STATUS_TYPE_ERROR


class Priority(ModelMethodsMixin, setup.Base):
    """Turn or queue priorities"""

    __tablename__ = "priorities"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    code = Column(String(50))
    weight = Column(Integer)
    description = Column(String(500))
    is_active = Column(Boolean, default=True)
    __table_args__ = (
        UniqueConstraint("name", name="priority_name_unique"),
        UniqueConstraint("code", name="priority_code_unique"),
    )

class Location(ModelMethodsMixin, setup.Base):
    """Turn or queue locations"""

    __tablename__ = "locations"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    code = Column(String(50))
    address = Column(String(500))
    description = Column(String(500))
    is_active = Column(Boolean, default=True)
    __table_args__ = (
        UniqueConstraint("name", name="location_name_unique"),
        UniqueConstraint("code", name="location_code_unique"),
    )


class Category(ModelMethodsMixin, setup.Base):
    """Categories are higher-level classification
    or grouping of customers
    or visitors based on the nature or purpose of their visit.
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
    __table_args__ = (
        UniqueConstraint("name", name="category_name_unique"),
        UniqueConstraint("code", name="category_code_unique"),
    )


class Service(ModelMethodsMixin, setup.Base):
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
    __table_args__ = (
        UniqueConstraint("name", name="service_name_unique"),
        UniqueConstraint("code", name="service_code_unique"),
        UniqueConstraint("prefix", name="service_prefix_unique"),
    )


class Customer(ModelMethodsMixin, setup.Base):
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
    gender = Column(Enum(*enums.Gender.get_values()))
    year_of_birth = Column(Integer)
    status_id = mapped_column(ForeignKey("statuses.id"))
    status = relationship("Status")
    created = Column(DateTime(timezone=True), server_default=func.now())
    created_by = Column(String(50))
    last_modified = Column(DateTime(timezone=True), onupdate=func.now())
    last_modified_by = Column(String(50))
    __table_args__ = (
        UniqueConstraint("email", name="customer_email_unique"),
    )


class Appointment(ModelMethodsMixin, setup.Base):
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


class ServiceTurn(ModelMethodsMixin, setup.Base):
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
    __table_args__ = (
        UniqueConstraint("ticket_number", name="turn_ticket_number_unique"),
    )


class Queue(ModelMethodsMixin, setup.Base):
    """Queues are sequence of customers
    or individuals waiting for a service or assistance.
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
    __table_args__ = (
        UniqueConstraint("name", name="queue_name_unique"),
        UniqueConstraint("code", name="queue_code_unique"),
    )
