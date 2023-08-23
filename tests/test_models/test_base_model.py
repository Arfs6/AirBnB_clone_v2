#!/usr/bin/python3
"""Test module for the base_model module."""
import unittest
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from models.base_model import BaseModel
from models import isDBStorage, storage


class TestBaseModel(unittest.TestCase):
    """Unit test test case for the BaseModel class"""

    def test_new_instance_has_id(self):
        """Tests if the new instance has an id attribute"""
        # Create a new instance of BaseModel
        model = BaseModel()
        # Ensure that the ID is generated and is a string
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.id, str)

    def test_created_at_and_updated_at_are_datetime(self):
        """Test if created_at and updated_at attributes"""
        # Create a new instance of BaseModel
        model = BaseModel()
        # Check if created_at and updated_at are datetime objects
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        # Create a new instance of BaseModel
        model = BaseModel()
        # Call the to_dict method
        model_dict = model.to_dict()
        # Check if the returned dictionary has the expected keys
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        for key in expected_keys:
            self.assertIn(key, model_dict)

    @unittest.skipIf(isDBStorage, "Cannot perform this test for db storage")
    def test_save_method_updates_updated_at(self):
        "test the save method."
        # Create a new instance of BaseModel
        model = BaseModel()
        original_updated_at = model.updated_at
        # Call the save method
        model.save()
        # Check if updated_at has been updated
        self.assertNotEqual(original_updated_at, model.updated_at)

    @unittest.skipUnless(isDBStorage, "test only works for DB storage")
    def test_saveUpdates_updated_at(self):
        """Tests if the save method updates updated_at"""
        from models.state import State
        s = State()
        old = s.updated_at
        s.name = 'TestState'
        s.save()
        self.assertNotEqual(old, s.updated_at)

    @unittest.skipIf(isDBStorage, "Skipping tests for BaseModel save method since in db storage")
    def test_model_is_saved_after_save_method(self):
        # Create a new instance of BaseModel
        model = BaseModel()
        # Call the save method
        model.save()
        self.assertIn(model, storage.all().values())

    @unittest.skipUnless(isDBStorage, "Skipping the save method test for db storage")
    def test_save_method_db(self):
        """Test the save method"""
        from models.state import State
        model = State()
        model.name = 'TestState'
        model.save()
        self.assertIn(model, storage.all().values())

    def test_str_representation(self):
        """Test the __str___ method."""
        # Create a new instance of BaseModel
        model = BaseModel()
        # Check if the __str__ method returns the expected format
        expected_format = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_format)

    def test_init_with_kwargs(self):
        """Test if initializing with kwargs works"""
        # Create a new instance of BaseModel with kwargs
        kwargs = {
            'id': '123',
            'created_at': '2023-08-22T12:00:00.0000',
            'updated_at': '2023-08-22T13:00:00.0000',
            'name': 'Test Model'
        }
        model = BaseModel(**kwargs)
        # Check if the provided kwargs are correctly set
        self.assertEqual(model.id, '123')
        self.assertEqual(model.created_at, datetime(2023, 8, 22, 12, 0, 0))
        self.assertEqual(model.updated_at, datetime(2023, 8, 22, 13, 0, 0))
        self.assertEqual(model.name, 'Test Model')

    @unittest.skipIf(isDBStorage, "Test specific for file storage")
    def test_deleteFileStorage(self):
        """test the delete method"""
        model = BaseModel()
        model.save()
        self.assertIn(model, storage.all().values())
        model.delete()
        self.assertNotIn(model, storage.all().values())

    @unittest.skipUnless(isDBStorage, "Can't test delete method from base model")
    def test_deleteDBStorage(self):
        """test the delete method in State for db class"""
        from models.state import State
        model = State()
        model.name = "TestState"
        model.save()
        self.assertIn(model, storage.all().values())
        model.delete()
        storage.save()
        self.assertNotIn(model, storage.all().values())

    def test_clsAttributes(self):
        """Test all the class attributes"""
        self.assertTrue(hasattr(BaseModel, 'id'))
        self.assertTrue(BaseModel.id.primary_key == True)
        self.assertTrue(BaseModel.id.nullable == False)
        self.assertTrue(BaseModel.created_at.nullable == False)


if __name__ == '__main__':
    unittest.main()
