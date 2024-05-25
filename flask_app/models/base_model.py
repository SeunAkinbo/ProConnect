#!/usr/bin/python3

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
import uuid

Base = declarative_base()

class BaseModel:
    """A base class for all ProConnect models"""
    id = Column(String(60), primary_key=True, default=lambda: str(uuid.uuid4()))

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """Saves the model to the storage"""
        from models import storage
        storage.new(self)
        storage.save()

    def delete(self):
        """Deletes the model from the storage"""
        from models import storage
        storage.delete(self)
