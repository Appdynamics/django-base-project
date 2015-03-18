"""
[1]: http://model-mommy.readthedocs.org/en/stable/basic_usage.html
"""

# Core Django imports
from django.test import TestCase

# Third-party app imports
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key

# Relative imports of the 'app-name' package
from {{ project_name }}.sample_app.models import Kid

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