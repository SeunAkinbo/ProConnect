#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Service(BaseModel, Base):
    """This class defines a service by various attributes"""
    __tablename__ = 'services'
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
