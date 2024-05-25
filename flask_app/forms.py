#!/usr/bin/python3
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SelectField, EmailField, URLField
from wtforms.validators import DataRequired, Email, URL

class UpdateProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    avatar = FileField('Avatar', validators=[])
    address = StringField('Address', validators=[DataRequired()])
    payment = SelectField('Payment Option', choices=[('currency', 'Currency'), ('skill', 'Skill'), ('both', 'Both')], validators=[DataRequired()])
    availability = SelectField('Availability', choices=[('physical', 'Physical'), ('remote', 'Remote'), ('both', 'Both')], validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    linkedin = URLField('LinkedIn', validators=[DataRequired(), URL()])
    github = URLField('GitHub', validators=[DataRequired(), URL()])
    reviews = TextAreaField('Reviews/Endorsements', validators=[DataRequired()])
