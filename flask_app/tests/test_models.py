#!/usr/bin/python3
"""Unittest models Module"""
from unittest import TestCase
from models import User, Field, Category, Profile, Skill


class TestUser(TestCase):
    """Tests the User class"""
    def test_user_creation(self):
        user = User(username='testuser', email='test@example.com')
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')

    def test_user_password_hashing(self):
        password = 'testpassword'
        user = User(username='testuser', email='test@example.com', password=password)
        self.assertNotEqual(user.password_hash, password)
        self.assertTrue(user.verify_password(password))

    def test_user_password_verification_failure(self):
        password = 'testpassword'
        user = User(username='testuser', email='test@example.com', password=password)
        self.assertFalse(user.verify_password('wrongpassword'))

    def test_user_avatar(self):
        user = User(username='testuser', email='test@example.com')
        self.assertTrue(user.avatar(128))

    def test_user_follow(self):
        user1 = User(username='user1', email='user1@example.com')
        user2 = User(username='user2', email='user2@example.com')
        self.assertFalse(user1.is_following(user2))
        user1.follow(user2)
        self.assertTrue(user1.is_following(user2))
        self.assertIn(user2, user1.followed)
        self.assertIn(user1, user2.followers)

    def test_user_unfollow(self):
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
        field = Field(name='Test Field', description='This is a test field')
        self.assertIsInstance(field, Field)
        self.assertEqual(field.name, 'Test Field')
        self.assertEqual(field.description, 'This is a test field')

    def test_field_categories(self):
        category1 = Category(name='Category 1')
        category2 = Category(name='Category 2')
        field = Field(name='Test Field', categories=[category1, category2])
        self.assertIn(category1, field.categories)
        self.assertIn(category2, field.categories)

    def test_field_profiles(self):
        profile1 = Profile(name='Profile 1')
        profile2 = Profile(name='Profile 2')
        field = Field(name='Test Field', profiles=[profile1, profile2])
        self.assertIn(profile1, field.profiles)
        self.assertIn(profile2, field.profiles)


class TestCategory(TestCase):
    """Test the Category class"""
    def test_category_creation(self):
        category = Category(name='Test Category')
        self.assertIsInstance(category, Category)
        self.assertEqual(category.name, 'Test Category')

    def test_category_fields(self):
        field1 = Field(name='Field 1')
        field2 = Field(name='Field 2')
        category = Category(name='Test Category', fields=[field1, field2])
        self.assertIn(field1, category.fields)
        self.assertIn(field2, category.fields)


class TestProfile(TestCase):
    """Test the Profile class"""
    def test_profile_creation(self):
        profile = Profile(name='Test Profile')
        self.assertIsInstance(profile, Profile)
        self.assertEqual(profile.name, 'Test Profile')

    def test_profile_fields(self):
        field1 = Field(name='Field 1')
        field2 = Field(name='Field 2')
        profile = Profile(name='Test Profile', fields=[field1, field2])
        self.assertIn(field1, profile.fields)
        self.assertIn(field2, profile.fields)


class TestSkill(TestCase):
    """Test the Skill class"""
    def test_skill_creation(self):
        skill = Skill(name='Python', description='Programming language')
        self.assertIsInstance(skill, Skill)
        self.assertEqual(skill.name, 'Python')
        self.assertEqual(skill.description, 'Programming language')

    def test_skill_users(self):
        user1 = User(username='user1', email='user1@example.com')
        user2 = User(username='user2', email='user2@example.com')
        skill = Skill(name='Python', users=[user1, user2])
        self.assertIn(user1, skill.users)
        self.assertIn(user2, skill.users)

    def test_skill_profiles(self):
        profile1 = Profile(name='Profile 1')
        profile2 = Profile(name='Profile 2')
        skill = Skill(name='Python', profiles=[profile1, profile2])
        self.assertIn(profile1, skill.profiles)
        self.assertIn(profile2, skill.profiles)

    def test_skill_categories(self):
        category1 = Category(name='Category 1')
        category2 = Category(name='Category 2')
        skill = Skill(name='Python', categories=[category1, category2])
        self.assertIn(category1, skill.categories)
        self.assertIn(category2, skill.categories)

    def test_skill_fields(self):
        field1 = Field(name='Field 1')
        field2 = Field(name='Field 2')
        skill = Skill(name='Python', fields=[field1, field2])
        self.assertIn(field1, skill.fields)
        self.assertIn(field2, skill.fields)
