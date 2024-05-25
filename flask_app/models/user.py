#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)

    profiles = relationship("Profile", backref="user", cascade="all, delete, delete-orphan")
    skills = relationship("Skill", backref="user", cascade="all, delete, delete-orphan")
