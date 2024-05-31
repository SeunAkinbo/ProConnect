#!/usr/bin/python3
"""
This module contains unit tests for the forms used in the Flask application.

The `TestLoginForm` class tests the validation of the `LoginForm` form, including
valid and invalid email addresses, and missing email or password fields.

The `TestRegistrationForm` class tests the validation of the `RegistrationForm`
form, including valid registration data, invalid email addresses, and mismatched
passwords.

The `TestSkillForm` class tests the validation of the `SkillForm` form, including
a valid skill and a missing skill.

The `TestUpdateProfileForm` class tests the validation of the `UpdateProfileForm`
form, including valid profile updates and an invalid email address.
"""
from unittest import TestCase
from flask_app.forms import LoginForm, RegistrationForm, SkillForm, UpdateProfileForm


class TestLoginForm(TestCase):
    """Tests LoginForm class validation"""
    def test_valid_login_form(self):
        """Tests for login form validation"""
        form = LoginForm(data={'email': 'test@example.com', 'password': 'password'})
        self.assertTrue(form.validate())

    def test_invalid_email_login_form(self):
        """Tests for invalid email login form validation"""
        form = LoginForm(data={'email': 'invalid_email', 'password': 'password'})
        self.assertFalse(form.validate())

    def test_missing_email_login_form(self):
        """Tests for missing emails on LoginForm"""
        form = LoginForm(data={'email': '', 'password': 'password'})
        self.assertFalse(form.validate())

    def test_missing_password_login_form(self):
        """Tests for missing password on LoginForm"""
        form = LoginForm(data={'email': 'test@example.com', 'password': ''})
        self.assertFalse(form.validate())

class TestRegistrationForm(TestCase):
    """Tests for registration form"""
    def test_valid_registration_form(self):
        """Tests for a valid registration"""
        form = RegistrationForm(data={'username': 'testuser', 'email': 'test@example.com', 'password': 'password', 'confirm_password': 'password'})
        self.assertTrue(form.validate())

    def test_invalid_email_registration_form(self):
        """Tests for a invalid email registration"""
        form = RegistrationForm(data={'username': 'testuser', 'email': 'invalid_email', 'password': 'password', 'confirm_password': 'password'})
        self.assertFalse(form.validate())

    def test_mismatched_passwords_registration_form(self):
        """Tests for a mismatched password registration"""
        form = RegistrationForm(data={'username': 'testuser', 'email': 'test@example.com', 'password': 'password', 'confirm_password': 'different_password'})
        self.assertFalse(form.validate())

class TestSkillForm(TestCase):
    """Unittest for the SkillForm"""
    def test_valid_skill_form(self):
        """Tests for valid skill form"""
        form = SkillForm(data={'skill': 'Python'})
        self.assertTrue(form.validate())

    def test_missing_skill_form(self):
        """Tests for missing skill form"""
        form = SkillForm(data={'skill': ''})
        self.assertFalse(form.validate())

class TestUpdateProfileForm(TestCase):
    """Tests for update profile form"""
    def test_valid_update_profile_form(self):
        """Tests for a valid updated profile form"""
        form = UpdateProfileForm(data={'username': 'newusername', 'email': 'new@example.com'})
        self.assertTrue(form.validate())

    def test_invalid_email_update_profile_form(self):
        """Tests for invalid email update profile form"""
        form = UpdateProfileForm(data={'username': 'newusername', 'email': 'invalid_email'})
        self.assertFalse(form.validate())
