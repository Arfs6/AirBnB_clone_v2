#!/usr/bin/python3
"""Initialization of models package."""
from os import getenv

IsDBStorage = False
if getenv('HBNB_TYPE_STORAGE') == 'db':
    from .engine.db_storage import DBStorage
    storage = DBStorage()
    IsDBStorage = True
else:
    from .engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
