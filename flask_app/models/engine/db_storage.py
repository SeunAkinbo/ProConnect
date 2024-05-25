#!/usr/bin/python3
"""
Contains the class DBStorage for ProConnect
"""

import models
from models.base_model import BaseModel, Base
from models.user import User
from models.skill import Skill
from models.service import Service
from models.review import Review
from models.profile import Profile
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"User": User, "Skill": Skill, "Service": Service, "Review": Review, "Profile": Profile}

class DBStorage:
    """Interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        PROCONN_MYSQL_USER = getenv('PROCONN_MYSQL_USER')
        PROCONN_MYSQL_PWD = getenv('PROCONN_MYSQL_PWD')
        PROCONN_MYSQL_HOST = getenv('PROCONN_MYSQL_HOST')
        PROCONN_MYSQL_DB = getenv('PROCONN_MYSQL_DB')
        PROCONN_ENV = getenv('PROCONN_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(PROCONN_MYSQL_USER,
                                             PROCONN_MYSQL_PWD,
                                             PROCONN_MYSQL_HOST,
                                             PROCONN_MYSQL_DB))
        if PROCONN_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """Call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if value.id == id:
                return value

        return None

    def count(self, cls=None):
        """
        Count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
