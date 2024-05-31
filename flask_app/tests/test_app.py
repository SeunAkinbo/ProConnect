#!/usr/bin/python3
"""Unittest app Module"""
import app
from unittest import TestCase, main


class TestApp(TestCase):
    """TestApp class"""
    def setUp(self):
        self.app = app.create_app()
        self.client = self.app.test_client()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)

    def test_about_route(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Page', response.data)

    def test_404_error(self):
        response = self.client.get('/invalid_route')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Not Found', response.data)

    def test_post_request(self):
        data = {'name': 'John Doe', 'email': 'john@example.com'}
        response = self.client.post('/submit', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Form submitted successfully', response.data)

    def test_invalid_post_request(self):
        data = {'name': '', 'email': 'invalid_email'}
        response = self.client.post('/submit', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid form data', response.data)

if __name__ == '__main__':
    main()
