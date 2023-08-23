#!/usr/bin/python
from models.state import State
from models import storage
from models.city import City
class test:
    def setUp(self):
        """Create a new State instance for testing."""
        self.state = State()
        self.state.name = "TestState"
        self.state.save()

    def tearDown(self):
        """delete self.state"""
        self.state.delete()
        storage.save()

    def test_relationship_cities(self):
        """Test State-City relationship."""
        city = City()
        city.name = 'TestCity'
        city.state_id = self.state.id
        city.save()
        print(f"arfs6-- {[str(i) for i in self.state.cities]}")
        print(city in self.state.cities)

    def __init__(self):
        self.setUp()
        self.test_relationship_cities()
        self.tearDown()


test()
