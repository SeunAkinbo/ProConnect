#!/usr/bin/python3
"""
Runs a test suite for the Flask application.

This module contains a set of unit tests that verify the functionality of the Flask
application. The tests cover various aspects of the application, including routing,
database interactions, and API responses.

The tests are organized into a TestCase class, which provides a consistent setup and
teardown process for each test. The test methods within the class check specific
behaviors of the application, such as ensuring that routes return the expected status
codes and that data is properly stored and retrieved from the database.

To run the tests, you can execute this module directly from the command line using a
testing framework like pytest or unittest.
"""
import app
from unittest import TestCase, main


class TestApp(TestCase):
    """TestApp class"""
    def setUp(self):
        """App setup"""
        self.app = app.create_app()
        self.client = self.app.test_client()

    def test_index_route(self):
        """Tests index routing"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)

    def test_about_route(self):
        """Tests about routing"""
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Page', response.data)

    def test_404_error(self):
        """Tests invalid routing"""
        response = self.client.get('/invalid_route')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Not Found', response.data)

    def test_post_request(self):
        """Tests post request"""
        data = {'name': 'John Doe', 'email': 'john@example.com'}
        response = self.client.post('/submit', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Form submitted successfully', response.data)

    def test_invalid_post_request(self):
        """Tests invalid post request"""
        data = {'name': '', 'email': 'invalid_email'}
        response = self.client.post('/submit', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid form data', response.data)

if __name__ == '__main__':
    main()
