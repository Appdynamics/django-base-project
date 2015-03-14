"""
If your tests rely on database access such as creating or querying models, be sure to 
create your test classes as subclasses of django.test.TestCase rather than unittest.TestCase.

Using unittest.TestCase avoids the cost of running each test in a transaction and flushing 
the database, but if your tests interact with the database their behavior will vary based 
on the order that the test runner executes them. This can lead to unit tests that pass when 
run in isolation but fail when run in a suite.
"""
import logging
import unittest

from django.test import Client, SimpleTestCase, TestCase, LiveServerTestCase
from rest_framework import status

# http://selenium.googlecode.com/svn/trunk/docs/api/py/index.html
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

class SampleBaseTestCase(unittest.TestCase):
    """
    Simple test to see if the home page works, implemented as 
    a unittest.TestCase class.
    """

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
    """
    Simple test to see if the home page works, implemented as
    a django.test.SimpleTestCase class.
    """

    def test_home_page(self):        
        self.assertTrue(
            status.is_success(self.client.get('/').status_code)
        )


class SampleSeleniumTests(LiveServerTestCase):
    """
    Simple test to see if the home page works, implemented as
    a django.test.SimpleTestCase class.
    """

    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super(SampleSeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SampleSeleniumTests, cls).tearDownClass()

    def test_admin_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))

        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('username')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('password')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()

        timeout = 2
        WebDriverWait(self.selenium, timeout).until(
            lambda driver: driver.find_element_by_tag_name('body')
        )
