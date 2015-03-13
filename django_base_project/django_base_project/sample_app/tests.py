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

from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

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


class SampleSeleniumTests(LiveServerTestCase):
    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super(SampleSeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SampleSeleniumTests, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('myuser')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('secret')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()