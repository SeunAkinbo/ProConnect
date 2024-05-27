#!/usr/bin/python3
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FieldList, FormField, SubmitField, FileField, IntegerField, EmailField, URLField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, URL, Length, Optional, EqualTo
from models import User

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

class UpdateProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    avatar = FileField('Avatar', validators=[Optional()])
    address = StringField('Address', validators=[DataRequired()])
    
    payment = SelectField('Payment Option', choices=[('currency', 'Currency'), ('skill', 'Skill'), ('both', 'Both')], validators=[DataRequired()])
    availability = SelectField('Availability', choices=[('physical', 'Physical'), ('remote', 'Remote'), ('both', 'Both')], validators=[DataRequired()])

    category = SelectField('Category', choices=[], validators=[DataRequired()])  # Choices will be filled in the view
    
    skills = FieldList(FormField(SkillForm), min_entries=1, validators=[DataRequired()])
    
    email = EmailField('Email', validators=[DataRequired(), Email()])
    linkedin = URLField('LinkedIn', validators=[DataRequired(), URL()])
    github = URLField('GitHub', validators=[DataRequired(), URL()])
    
    reviews = TextAreaField('Reviews/Endorsements', validators=[DataRequired()])
    
    submit = SubmitField('Update')
