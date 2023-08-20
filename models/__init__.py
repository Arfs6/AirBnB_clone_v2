#!/usr/bin/python3
"""Initialization of models package."""
from os import getenv

IsDbStorage = False
if getenv('HBNB_TYPE_STORAGE') == 'db':
    from .engine.db_storage import DBStorage
    storage = DBStorage()
    IsDbStorage = True
else:
    from .engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
from .state import State
from.city import City
from .review import Review
from .amenity import Amenity
from .user import User
from .place import Place
allModels = {
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State,
        'User': User,
        }
