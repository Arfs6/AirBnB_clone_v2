#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from . import isDBStorage, storage


City = None


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if isDBStorage:
        cities = relationship('City', back_populates='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Gets all the cities with state_id == self.id."""
            from . import getAllModels
            allModels = getAllModels()
            allCities = storage.all(allModels['City']).values()
            return [c for c in allCities if c.state_id == self.id]

    def __init__(self, *args, **kwargs):
        """Initialize table attrs"""
        global City
        from .city import City
        super().__init__(*args, **kwargs)
