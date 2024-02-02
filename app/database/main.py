"""Database entry
"""

from .setup import Base, engine, Session

Base.metadata.create_all(engine)

session = Session()
