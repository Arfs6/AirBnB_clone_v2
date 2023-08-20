#!/usr/bin/python3
"""MySQL database module."""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session as SessionType


class DBStorage:
    """An abstraction of the database"""
    __engine = None
    __session: SessionType = None

    def __init__(self):
        """Initialize database engine, session and all other necessary attributes"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        db = getenv('HBNB_MYSQL_DB')
        host = getenv('HBNB_MYSQL_HOST')
        url = f"mysql+mysqldb://{user}:{password}@{host}/{db}"
        self.__engine = create_engine(url, pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            from ..base_model import Base
            Base.metadata.drop_all()

    def all(self, cls=None):
        """Retrieves all stored models.
        Parameters:
        cls: If not None, return only instance of this class
        returns: dictionary of objects name as keys and objects as values.
        """
        if cls:
            query = self.__session.query(cls)
        else:
            query = self.__session.query('State')

        return {f"{obj.__class__.__name__}.{obj.id}" for obj in query.all()}

    def new(self, obj):
        """Add `obj` to session."""
        self.__session.add(obj)

    def save(self):
        """Commit all current changes from database"""
        self.__session.commit()

    def delete(self, obj):
        """Delete `obj` from __session"""
        self.__session.delete(obj)

    def reload(self):
        """Creates all tables.
        """
        from ..base_model import Base
        Base.metadata.create_all(self.__engine)
        SessionFactory = sessionmaker(
                bind=self.__engine, expire_on_commit=False, 
                )
        Session = scoped_session(SessionFactory)
        self.__session = Session()
