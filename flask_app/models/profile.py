#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Profile(BaseModel, Base):
    """This class defines a profile by various attributes"""
    __tablename__ = 'profiles'
    description = Column(String(1024), nullable=True)
    avatar = Column(String(256), nullable=True)
    email = Column(String(128), nullable=False)
    linkedin = Column(String(256), nullable=True)
    github = Column(String(256), nullable=True)
    address = Column(String(256), nullable=True)
    payment = Column(String(50), nullable=False)
    availability = Column(String(50), nullable=False)
    reviews = Column(String(2048), nullable=True)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    skills = relationship("Skill", backref="profile", cascade="all, delete, delete-orphan")
