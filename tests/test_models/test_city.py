#!/usr/bin/python3
"""Test module for State"""
import unittest

from models.city import City
from models.state import State
from models import storage, isDBStorage


class TestCity(unittest.TestCase):
    """Test City class"""

    def setUp(self):
        """Create a new City instance and add a State for testing."""
        self.state = State()
        self.state.name = "TestState"
        self.city = City()
        self.city.name = 'TestCity'
        self.city.state_id = self.state.id
        self.state.save()
        self.city.save()

    def tearDown(self):
        """Remove all test data from the database."""
        self.city.delete()
        self.state.delete()
        storage.save()

    def test_attributes(self):
        """Test City attributes."""
        self.assertEqual(self.city.name, "TestCity")
        self.assertEqual(self.city.state_id, self.state.id)

    def test_relationship_state(self):
        """Test City-State relationship."""
        self.assertIn(self.city, self.state.cities)
        if not isDBStorage:
            unittest.skip("File storage doesn't have City.state attribute")
            return
        self.assertEqual(self.city.state, self.state)

    def test_to_dict_method(self):
        """Test City to_dict method."""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['id'], self.city.id)
        self.assertEqual(city_dict['name'], self.city.name)
        self.assertEqual(city_dict['state_id'], self.city.state_id)
        self.assertEqual(city_dict['__class__'], "City")


if __name__ == '__main__':
    unittest.main()
