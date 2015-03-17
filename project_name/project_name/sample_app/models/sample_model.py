"""
A model is the single, definitive source of data about your data. It contains the essential fields
and behaviors of the data you’re storing. Django follows the DRY Principle. The goal is to define your 
data model in one place and automatically derive things from it.

This includes the migrations - unlike in Ruby On Rails, for example, migrations are entirely derived 
from your models file, and are essentially just a history that Django can roll through to update your
database schema to match your current models.

In this sample model, we create the same models referenced from model-mommy's documentation so that
we can show the power of testing with your models via model-mommy.

[1]: http://model-mommy.readthedocs.org/en/stable/basic_usage.html
"""

from django.db import models

class Kid(models.Model):
    """
    Model class Kid of family app
    """
    happy = models.BooleanField()
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    bio = models.TextField()
    wanted_games_qtd = models.BigIntegerField()
    birthday = models.DateField()
    appointment = models.DateTimeField()

    class Meta:
        verbose_name = u'Kid'
        verbose_name_plural = u'Kids'

    def __unicode__(self):
        """
        Return the name of kid
        """
        return u'%s' % (self.name)

class Dog(models.Model):
    """
    Model class Dog of family app
    """
    owner = models.ForeignKey('Kid')