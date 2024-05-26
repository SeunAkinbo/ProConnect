#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    profiles = db.relationship('Profile', backref='category', lazy=True)

class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    avatar = db.Column(db.String(200), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    payment = db.Column(db.String(100), nullable=True)
    availability = db.Column(db.String(100), nullable=True)
    linkedin = db.Column(db.String(200), nullable=True)
    github = db.Column(db.String(200), nullable=True)
    reviews = db.Column(db.Text, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    skills = db.relationship('Skill', backref='profile', lazy=True)

class Skill(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(100), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    category = db.relationship('Category', backref=db.backref('skills', lazy=True))
    
