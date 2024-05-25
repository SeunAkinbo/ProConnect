#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer

class Review(BaseModel, Base):
    """This class defines a review by various attributes"""
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    rating = Column(Integer, nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    service_id = Column(String(60), ForeignKey('services.id'), nullable=False)
