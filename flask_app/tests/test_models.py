#!/usr/bin/python3
"""
Defines the `User` model for the Flask application.

The `User` model represents a user of the application, with fields for the user's email, password, and whether the user is an admin.
"""

from unittest import TestCase
from flask_app.models import User, Field, Category, Profile, Skill


class TestUser(TestCase):
    """Tests the User class"""
    def test_user_creation(self):
        """Test the User class creation"""
        user = User(username='testuser', email='test@example.com')
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')

    def test_user_password_hashing(self):
        """Tests the User password hashing"""
        password = 'testpassword'
        user = User(username='testuser', email='test@example.com', password=password)
        self.assertNotEqual(user.password_hash, password)
        self.assertTrue(user.verify_password(password))

    def test_user_password_verification_failure(self):
        """Tests the User password verification failure"""
        password = 'testpassword'
        user = User(username='testuser', email='test@example.com', password=password)
        self.assertFalse(user.verify_password('wrongpassword'))

    def test_user_avatar(self):
        """Tests the User avatar"""
        user = User(username='testuser', email='test@example.com')
        self.assertTrue(user.avatar(128))

    def test_user_follow(self):
        """Tests the User follow"""
        user1 = User(username='user1', email='user1@example.com')
        user2 = User(username='user2', email='user2@example.com')
        self.assertFalse(user1.is_following(user2))
        user1.follow(user2)
        self.assertTrue(user1.is_following(user2))
        self.assertIn(user2, user1.followed)
        self.assertIn(user1, user2.followers)

    def test_user_unfollow(self):
        """Tests that user unfollows"""
        user1 = User(username='user1', email='user1@example.com')
        user2 = User(username='user2', email='user2@example.com')
        user1.follow(user2)
        self.assertTrue(user1.is_following(user2))
        user1.unfollow(user2)
        self.assertFalse(user1.is_following(user2))
        self.assertNotIn(user2, user1.followed)
        self.assertNotIn(user1, user2.followers)


class TestField(TestCase):
    """Test the Field class"""
    def test_field_creation(self):
        """Tests the Field class creation"""
        field = Field(name='Test Field', description='This is a test field')
        self.assertIsInstance(field, Field)
        self.assertEqual(field.name, 'Test Field')
        self.assertEqual(field.description, 'This is a test field')

    def test_field_categories(self):
        """Tests the Field class categories"""
        category1 = Category(name='Category 1')
        category2 = Category(name='Category 2')
        field = Field(name='Test Field', categories=[category1, category2])
        self.assertIn(category1, field.categories)
        self.assertIn(category2, field.categories)

    def test_field_profiles(self):
        """Tests Field profiles"""
        profile1 = Profile(name='Profile 1')
        profile2 = Profile(name='Profile 2')
        field = Field(name='Test Field', profiles=[profile1, profile2])
        self.assertIn(profile1, field.profiles)
        self.assertIn(profile2, field.profiles)


class TestCategory(TestCase):
    """Test the Category class"""
    def test_category_creation(self):
        """Tests Category class creation"""
        category = Category(name='Test Category')
        self.assertIsInstance(category, Category)
        self.assertEqual(category.name, 'Test Category')

    def test_category_fields(self):
        """Tests Category fields creation"""
        field1 = Field(name='Field 1')
        field2 = Field(name='Field 2')
        category = Category(name='Test Category', fields=[field1, field2])
        self.assertIn(field1, category.fields)
        self.assertIn(field2, category.fields)


class TestProfile(TestCase):
    """Test the Profile class"""
    def test_profile_creation(self):
        """Tests Profile class creation"""
        profile = Profile(name='Test Profile')
        self.assertIsInstance(profile, Profile)
        self.assertEqual(profile.name, 'Test Profile')

    def test_profile_fields(self):
        """Tests Profile fields creation"""
        field1 = Field(name='Field 1')
        field2 = Field(name='Field 2')
        profile = Profile(name='Test Profile', fields=[field1, field2])
        self.assertIn(field1, profile.fields)
        self.assertIn(field2, profile.fields)


class TestSkill(TestCase):
    """Test the Skill class"""
    def test_skill_creation(self):
        """Tests the Skill class creation"""
        skill = Skill(name='Python', description='Programming language')
        self.assertIsInstance(skill, Skill)
        self.assertEqual(skill.name, 'Python')
        self.assertEqual(skill.description, 'Programming language')

    def test_skill_users(self):
        """Tests Skill class for the users"""
        user1 = User(username='user1', email='user1@example.com')
        user2 = User(username='user2', email='user2@example.com')
        skill = Skill(name='Python', users=[user1, user2])
        self.assertIn(user1, skill.users)
        self.assertIn(user2, skill.users)

    def test_skill_profiles(self):
        """Tests the Skill in profiles"""
        profile1 = Profile(name='Profile 1')
        profile2 = Profile(name='Profile 2')
        skill = Skill(name='Python', profiles=[profile1, profile2])
        self.assertIn(profile1, skill.profiles)
        self.assertIn(profile2, skill.profiles)

    def test_skill_categories(self):
        """Tests for Skill in category"""
        category1 = Category(name='Category 1')
        category2 = Category(name='Category 2')
        skill = Skill(name='Python', categories=[category1, category2])
        self.assertIn(category1, skill.categories)
        self.assertIn(category2, skill.categories)

    def test_skill_fields(self):
        """Tests for Skill in fields"""
        field1 = Field(name='Field 1')
        field2 = Field(name='Field 2')
        skill = Skill(name='Python', fields=[field1, field2])
        self.assertIn(field1, skill.fields)
        self.assertIn(field2, skill.fields)
