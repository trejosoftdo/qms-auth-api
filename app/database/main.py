"""Database entry
"""

from sqlalchemy.orm import Session
from .setup import Base, engine, Session as DBSession

Base.metadata.create_all(engine)


def get_session() -> Session:
    """Gets a database session"""
    session = DBSession()
    try:
        yield session
    finally:
        session.close()
