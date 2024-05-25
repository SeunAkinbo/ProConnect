#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Skill(BaseModel, Base):
    """This class defines a skill by various attributes"""
    __tablename__ = 'skills'
    name = Column(String(128), nullable=False)
    duration = Column(String(128), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    profile_id = Column(String(60), ForeignKey('profiles.id'), nullable=False)
