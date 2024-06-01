#!/usr/bin/python3
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FieldList, FormField, SubmitField, FileField, IntegerField, EmailField, URLField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, URL, Length, Optional, EqualTo, ValidationError
from models import User, Field, Category

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')
    
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already in use.')
     
class SkillForm(FlaskForm):
    skill_name = StringField('Skill Name', validators=[DataRequired()])
    duration = StringField('Duration (e.g., 5 years)', validators=[DataRequired()])

class NoneIfEmpty(Optional):
    def __call__(self, form, field):
        if field.data == '':
            field.data = None
        Optional.__call__(self, form, field)

class Unique(object):
    def __init__(self, model, field, message="This element already exists."):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)
        
class UpdateProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    avatar = FileField('Avatar', validators=[Optional()])
    address = StringField('Address', validators=[DataRequired()])
    payment = SelectField('Payment Option', choices=[('currency', 'Currency'), ('skill', 'Skill'), ('both', 'Both')], validators=[DataRequired()])
    availability = SelectField('Availability', choices=[('physical', 'Physical'), ('remote', 'Remote'), ('both', 'Both')], validators=[DataRequired()])
    field = SelectField('Field', choices=[], validators=[DataRequired()])
    category = SelectField('Category', choices=[], validators=[DataRequired()])
    skills = FieldList(FormField(SkillForm), min_entries=1, max_entries=1, validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    linkedin = URLField('LinkedIn', validators=[DataRequired(), URL()])
    github = URLField('GitHub', validators=[NoneIfEmpty()])
    reviews = TextAreaField('Reviews/Endorsements', validators=[NoneIfEmpty()])
    
    submit = SubmitField('Update_profile')
