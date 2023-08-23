#!/usr/bin/python3
"""Test cases for the state module"""
import unittest
from sqlalchemy import Column
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models import isDBStorage, storage


class TestState(unittest.TestCase):
    """Test the State class"""

    def setUp(self):
        """Create a new State instance for testing."""
        self.state = State()
        self.state.name = "TestState"
        self.state.save()

    def tearDown(self):
        """delete self.state"""
        self.state.delete()
        storage.save()

    def test_inheritance(self):
        """Test if State inherits from BaseModel and Base."""
        self.assertIsInstance(self.state, BaseModel)
        self.assertIsInstance(self.state, Base)

    def test_attributes(self):
        """Test State attributes."""
        self.assertEqual(self.state.name, "TestState")

    def test_relationship_cities(self):
        """Test State-City relationship."""
        city = City()
        city.name = 'TestCity'
        city.state_id = self.state.id
        city.save()
        self.assertIn(city, self.state.cities)

    def test_to_dict_method(self):
        """Test State to_dict method."""
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['id'], self.state.id)
        self.assertEqual(state_dict['name'], self.state.name)
        self.assertEqual(state_dict['__class__'], "State")

    def test_clsCommonAttributes(self):
        """Test all the common class attributes"""
        self.assertTrue(State.name.nullable == False)


if __name__ == '__main__':
    unittest.main()
