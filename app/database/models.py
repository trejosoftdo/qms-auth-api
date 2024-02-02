"""Database models
"""

from sqlalchemy import Column, Integer, String, Sequence
from . import setup


class Status(setup.Base):
    __tablename__ = "statuses"
    id = Column(Integer, Sequence("status_id"))
    name = Column(String(50))
