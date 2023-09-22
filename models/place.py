#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from . import isDBStorage, storage


# To avoid import circle, import it when initializing
Amenity = User = City = Review = None


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
    if isDBStorage:
        place_amenity = Table(
                'place_amenity',
                Base.metadata,
                Column(
                    'place_id', String(60), ForeignKey('places.id'),

                    primary_key=True, nullable=False),
                Column(
                    'amenity_id', String(60),
                    ForeignKey('amenities.id'), primary_key=True,
                    nullable=False)
                )
        amenities = relationship('Amenity', secondary='place_amenity',
                                 viewonly=False,
                                 back_populates='place_amenities')
        reviews = relationship('Review', back_populates='place',
                               cascade='all, delete-orphan')
    else:
        @property
        def amenities(self):
            """Returns amenities for file storage"""
            from . import getAllModels
            allModels = getAllModels()
            allAmenities = storage.all(allModels['Amenity'])
            return [a for a in allAmenities if a.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            """Append values to Amenity_ids"""
            from . import getAllModels
            allModels = getAllModels()
            if isinstance(value, allModels['Amenity']):
                self.amenity_ids.append(value.id)

        @property
        def reviews(self):
            """Reviews for file storage"""
            from . import getAllModels
            allModels = getAllModels()
            allReviews = storage.all(allModels['Review']).values()
            return [r for r in allReviews if r.place_id == self.id]

    def __init__(self, *args, **kwargs):
        """Initialize Place mapper"""
        global Amenity, User, City, Review
        from .review import Review
        from .user import User
        from .city import City
        from .amenity import Amenity
        super().__init__(*args, **kwargs)
