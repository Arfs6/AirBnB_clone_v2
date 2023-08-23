#!/usr/bin/python3
"""Test module for Place class"""
import unittest
from sqlalchemy.sql.schema import Column

from models import getAllModels
from models.place import Place
from models.base_model import BaseModel, Base


class TestPlace(unittest.TestCase):
    """Test the place class"""

    def setUp(self):
        """Create necessary attributes for testing"""
        self.place = Place()
        self.state = getAllModels()['State']()
        self.city = getAllModels()['City']()
        self.city.name = 'TestCity'
        self.user = getAllModels()['User']()
        self.state.name = 'TestState'
        self.state.save()
        self.city.state_id = self.state.id
        self.city.save()
        self.place.city_id = self.city.id
        self.user.email = 'student@alxswe.com'
        self.user.password = 'userpwd'
        self.user.save()
        self.place.user_id = self.user.id
        self.place.name = 'ALX campus'
        self.place.save()

    def tearDown(self):
        """Delete all created attributes"""
        self.state.delete()
        self.user.delete()

    def test_inheritance(self):
        """Test if Place inherits from BaseModel and Base"""
        self.assertTrue(issubclass(Place, Base))
        self.assertTrue(issubclass(Place, Base))

    def test_clsAttributes(self):
        """ Test all the class attributes """
        self.assertEqual(getattr(Place, '__tablename__'), 'places')
        self.assertTrue(Place.id.primary_key)
        self.assertFalse(Place.id.nullable)
        self.assertFalse(Place.name.nullable)
        self.assertFalse(Place.city_id.nullable)
        self.assertFalse(Place.user_id.nullable)
        self.assertTrue(Place.description.nullable)
        self.assertFalse(Place.number_rooms.nullable)
        self.assertFalse(Place.number_bathrooms.nullable)
        self.assertFalse(Place.max_guest.nullable)
        self.assertFalse(Place.price_by_night.nullable)
        self.assertTrue(Place.latitude.nullable)
        self.assertTrue(Place.longitude.nullable)
        self.assertTrue(isinstance(Place.amenity_ids, list))

    def test_relationship(self):
        """Test all the relationships of Place."""


if __name__ == '__main__':
    unittest.main()
