#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    avatar = db.Column(db.String(256))  # Assuming it's a URL or path
    address = db.Column(db.String(256), nullable=False)
    payment = db.Column(db.String(64), nullable=False)
    availability = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    linkedin = db.Column(db.String(256), unique=True, nullable=False)
    github = db.Column(db.String(256), unique=True, nullable=False)
    reviews = db.Column(db.Text, nullable=False)
    skills = db.relationship('Skill', backref='profile', lazy=True)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(128), nullable=False)
    duration = db.Column(db.String(64), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
