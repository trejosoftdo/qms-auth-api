"""Database setup
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.environment import database_connection_string

engine = create_engine(database_connection_string)
Base = declarative_base()
Session = sessionmaker(bind=engine)
