"""
[1]: http://model-mommy.readthedocs.org/en/stable/basic_usage.html
"""

# Core Django imports
from django.test import TestCase

# Third-party app imports
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key

# Relative imports of the 'app-name' package
from {{ project_name }}.sample_app.models import Kid, Dog

class KidTestModel(TestCase):
    """
    Class to test the model
    Kid
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.kid = mommy.make(Kid)

    def test_creating_multiple_kids(self):
        kids = mommy.make(Kid, _quantity=3)
        assert len(kids) == 3

class DogTestModel(TestCase):
    """
    Class to test the model
    Dog
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.rex = mommy.make(Dog)


class KidTestModel(TestCase):
    """
    Class to test the model
    Kid
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.kid = mommy.make(Kid)

    def test_kid_creation(self):
    	assert self.kid != None

    def test_creating_multiple_kids(self):
        kids = mommy.make(Kid, _quantity=3)
        assert len(kids) == 3

class DogTestModel(TestCase):
    """
    Class to test the model
    Dog
    """

    def setUp(self):
        """
        Set up all the tests
        """
        self.rex = mommy.make(Dog)

    def test_dog_creation(self):
    	assert self.rex != None

    def test_creating_multiple_dogs(self):
        dogs = mommy.make(Dog, _quantity=3)
        assert len(dogs) == 3
        
        for dog in dogs:
            assert dog.owner != None
