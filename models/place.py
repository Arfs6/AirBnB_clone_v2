#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from . import IsDBStorage, storage


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    # relationships
    user = relationship('User', back_populates='places')
    cities = relationship('City', back_populates='places')
    if isDBstorage:
        reviews = relationship('Review', back_populates='place', cascade='all, delete-orphan')
    else:
        @property
        def reviews(self):
            """Reviews for file storage"""
            allReviews = storage.all(type(self)).values()
            return [r for r in allReviews if r.place_id == self.id]
