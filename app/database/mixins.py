"""Database mixins
"""

from typing import Type, TypeVar, List, Callable
from sqlalchemy import select
from sqlalchemy.sql import Select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from app import exceptions
from . import setup
from . import helpers


T = TypeVar("T", bound=setup.Base)


class ModelMethodsMixin:
    """Model Methods Mixin"""

    @classmethod
    def find_by_id(cls: Type[T], session: Session, entity_id: int) -> T:
        """Gets an entity by id

        Args:
            session (Session): Database session
            entity_id (int): ID of entity

        Returns:
            T: The matched entity
        """
        try:
            statement = select(cls).where(cls.id == entity_id).limit(1)
            return session.scalars(statement).one()
        except NoResultFound as exc:
            session.rollback()
            raise exceptions.NOT_FOUND_ERROR from exc
        except:
            session.rollback()
            raise

    @classmethod
    def find_one(
        cls: Type[T], session: Session, filter_selection: Callable[[Select], Select]
    ) -> T:
        """Gets an entity by filter

        Args:
            session (Session): Database session
            filter_selection (Callable[[Any], Any]): Filter func

        Returns:
            T: The matched entity
        """
        try:
            statement = select(cls)
            selection = filter_selection(statement).limit(1)
            return session.scalars(selection).one()
        except NoResultFound as exc:
            session.rollback()
            raise exceptions.NOT_FOUND_ERROR from exc
        except:
            session.rollback()
            raise

    @classmethod
    def find_many(
        cls: Type[T],
        session: Session,
        filter_selection: Callable[[Select], Select] = None,
    ) -> List[T]:
        """Find many items in a paginated manner

        Args:
            session (Session): Database session
            filter_selection (Callable[[Any], Any]): Filter func

        Returns:
            List[T]: The matched entities
        """
        try:
            selection = select(cls)

            if callable(filter_selection):
                selection = filter_selection(selection)

            return session.scalars(selection)
        except:
            session.rollback()
            raise

    @classmethod
    def find_paginated(
        cls: Type[T],
        session: Session,
        limit: int,
        offset: int,
        filter_selection: Callable[[Select], Select] = None,
    ) -> List[T]:
        """Find many items in a paginated manner

        Args:
            session (Session): Database session
            limit (int): total number of items to be returned
            offset (int): starting offset position
            filter_selection (Callable[[Any], Any]): Filter func

        Returns:
            List[T]: The matched entities
        """
        try:
            selection = select(cls)

            if callable(filter_selection):
                selection = filter_selection(selection)

            statement = selection.limit(limit).offset(offset)

            return session.scalars(statement)
        except:
            session.rollback()
            raise

    @classmethod
    def create_from_data(cls: Type[T], session: Session, data: dict) -> T:
        """Creates an entity from the given data

        Args:
            session (Session): Database session
            data (dict): Entity data

        Returns:
            T: The created entity
        """
        item = cls(**helpers.snake_case_props(data))
        item.create(session)
        return item

    @classmethod
    def update_by_id(cls: Type[T], session: Session, entity_id: int, data: dict) -> T:
        """Gets an entity by id

        Args:
            session (Session): Database session
            entity_id (int): ID of entity
            data (dict): Update data

        Returns:
            T: The updated entity
        """
        item = cls.find_by_id(session, entity_id)
        item.set_values(helpers.snake_case_props(data))
        item.update(session)
        return item

    @classmethod
    def delete_by_id(cls: Type[T], session: Session, entity_id: int) -> T:
        """Deletes an entity by id

        Args:
            session (Session): Database session
            entity_id (int): ID of entity

        Returns:
            T: The deleted entity
        """
        item = cls.find_by_id(session, entity_id)
        item.delete(session)
        return item

    def to_dict(self: T) -> dict:
        """Transform the item into dictionary

        Args:
            self (T): Database model

        Returns:
            dict: The created dictionary
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def set_values(self: T, data: dict) -> None:
        """Sets properties values from data dictionary

        Args:
            data (dict): Data dictionary
        """
        for name in data:
            if (
                name != "id"
                and (name in self.__table__.columns)
                and not data[name] is None
            ):
                setattr(self, name, data[name])

    @helpers.handle_duplicate_error
    @helpers.handle_session_rollback
    def create(self: T, session: Session) -> None:
        """Creates a new item in the database

        Args:
            self (T): Database model
        """
        session.add(self)
        session.commit()

    @helpers.handle_duplicate_error
    @helpers.handle_session_rollback
    def update(self: T, session: Session) -> None:
        """Saves the changes made on the item

        Args:
            self (T): Database model
        """
        session.commit()

    @helpers.handle_duplicate_error
    @helpers.handle_session_rollback
    def delete(self: T, session: Session) -> None:
        """Deletes the current item from the database

        Args:
            self (T): Database model
        """
        session.delete(self)
        session.commit()
