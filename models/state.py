#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from . import IsDbStorage, storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if IsDbStorage:
        cities = relationship('City', back_populates='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Gets all the cities with state_id == self.id."""
            allCities = storage.all(type(self)).values()
            return list(allCities)
