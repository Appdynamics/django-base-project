"""
If your tests rely on database access such as creating or querying models, be sure to 
create your test classes as subclasses of django.test.TestCase rather than unittest.TestCase.

Using unittest.TestCase avoids the cost of running each test in a transaction and flushing 
the database, but if your tests interact with the database their behavior will vary based 
on the order that the test runner executes them. This can lead to unit tests that pass when 
run in isolation but fail when run in a suite.
"""
import unittest

from django.test import SimpleTestCase, TestCase, Client
from rest_framework import status

class SampleBaseTestCase(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertTrue(
        	status.is_success(response.status_code)
        )


class SampleSimpleTestCase(SimpleTestCase):

    def test_home_page(self):
        """
        Simple test to see if the home page works.
        """
        
        self.assertTrue(
        	status.is_success(self.client.get('/').status_code)
        )