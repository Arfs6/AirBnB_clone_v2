#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


State = None


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    def __init__(self, *args, **kwargs):
        """Initialize City mapper"""
        global State
        from .state import State
        super().__init__(*args, **kwargs)
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    # relationships
    state = relationship('State', back_populates='cities')
    places = relationship('Place', back_populates='cities',
                          cascade='all, delete-orphan')
