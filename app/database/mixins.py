"""Database mixins
"""

from typing import Type, TypeVar, List, Callable
from sqlalchemy import select
from sqlalchemy.sql import Select
from .. import helpers
from . import main
from . import setup


T = TypeVar("T", bound=setup.Base)


class ModelMethodsMixin:
    """Model Methods Mixin"""

    @classmethod
    def find_by_id(cls: Type[T], entity_id: int) -> T:
        """Gets an entity by id

        Args:
            entity_id (int): ID of entity

        Returns:
            T: The matched entity
        """
        statement = select(cls).where(cls.id == entity_id).limit(1)
        return main.session.scalars(statement).one()

    @classmethod
    def find_many(
        cls: Type[T],
        filter_selection: Callable[[Select], Select] = None,
    ) -> List[T]:
        """Find many items in a paginated manner

        Args:
            filter_selection (Callable[[Any], Any]): Filter func

        Returns:
            List[T]: The matched entities
        """
        selection = select(cls)

        if callable(filter_selection):
            selection = filter_selection(selection)

        return main.session.scalars(selection)

    @classmethod
    def find_paginated(
        cls: Type[T],
        limit: int,
        offset: int,
        filter_selection: Callable[[Select], Select] = None,
    ) -> List[T]:
        """Find many items in a paginated manner

        Args:
            limit (int): total number of items to be returned
            offset (int): starting offset position
            filter_selection (Callable[[Any], Any]): Filter func

        Returns:
            List[T]: The matched entities
        """
        selection = select(cls)

        if callable(filter_selection):
            selection = filter_selection(selection)

        statement = selection.limit(limit).offset(offset)

        return main.session.scalars(statement)

    @classmethod
    def create_from_data(cls: Type[T], data: dict) -> T:
        """Creates an entity from the given data

        Args:
            data (dict): Entity data

        Returns:
            T: The created entity
        """
        item = cls(**helpers.snake_case_props(data))
        item.create()
        return item

    @classmethod
    def update_by_id(cls: Type[T], entity_id: int, data: dict) -> T:
        """Gets an entity by id

        Args:
            entity_id (int): ID of entity
            data (dict): Update data

        Returns:
            T: The updated entity
        """
        item = cls.find_by_id(entity_id)
        item.set_values(helpers.snake_case_props(data))
        item.update()
        return item

    @classmethod
    def delete_by_id(cls: Type[T], entity_id: int) -> T:
        """Deletes an entity by id

        Args:
            entity_id (int): ID of entity

        Returns:
            T: The deleted entity
        """
        item = cls.find_by_id(entity_id)
        item.delete()
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

    def create(self: T) -> None:
        """Creates a new item in the database

        Args:
            self (T): Database model
        """
        main.session.add(self)
        main.session.commit()

    def update(self: T) -> None:
        """Saves the changes made on the item

        Args:
            self (T): Database model
        """
        main.session.commit()

    def delete(self: T) -> None:
        """Deletes the current item from the database

        Args:
            self (T): Database model
        """
        main.session.delete(self)
        main.session.commit()
