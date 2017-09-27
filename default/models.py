# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    type = models.CharField(max_length=100, default="admin", blank=False, null=False)
    location = models.CharField(max_length=100, blank=True, null=True)
    skype = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    photoURL =  models.CharField(max_length=250, blank=False, null=False)
    REQUIRED_FIELDS = ['type', 'email', 'first_name', 'last_name']


from .managers import AdminUserManager
class AdminUser(User):
    objects = AdminUserManager()

    class Meta:
        proxy = True
        ordering = ('first_name', )

    def do_something(self):
        pass

from .managers import ReviewerUserManager
class ReviewerUser(User):
    objects = ReviewerUserManager()

    class Meta:
        proxy = True
        ordering = ('first_name', )

    def do_something(self):
        pass

from .managers import AuthorUserManager
class AuthorUser(User):
    objects = AuthorUserManager()

    class Meta:
        proxy = True
        ordering = ('first_name', )

    def do_something(self):
        pass

class Conference(models.Model):
    id = models.AutoField(primary_key=True, help_text="conference id")
    name = models.CharField(max_length=20,  help_text="name of conference", unique=True)
    users = models.ManyToManyField(User)
    acronym = models.CharField(max_length=20,  help_text="acronym", unique=True)
    webpage = models.CharField(max_length=20,  help_text="web page", unique=True)
    city = models.CharField(max_length=200, help_text="Enter a city")
    country_id = models.IntegerField( help_text="country")
    start_date = models.DateTimeField(auto_now=False)
    end_date = models.DateTimeField(auto_now=False)
    contact_email = models.CharField(max_length=200, help_text="contact_emai")
    webpage = models.CharField(max_length=200, help_text="webpage")
    banner = models.CharField(max_length=200, help_text="banner")
    license_expiry = models.CharField(max_length=200, help_text="status")
    status = models.BooleanField(max_length=200, help_text="status")

    def __unicode__(self):
         return self.acronym

class Submission(models.Model):
    id = models.AutoField(primary_key=True, help_text="reviewer")
    conference = models.ForeignKey('Conference',on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, help_text="Enter a title")
    abstract = models.TextField( help_text="Enter a abstract")
    keywords = models.CharField(max_length=200, help_text="keywords")
    paper_url = models.CharField(max_length=200, help_text="paper url")
    status = models.CharField(max_length=200, help_text="status")

class Country(models.Model):
    id = models.AutoField(primary_key=True, help_text="reviewer")
    code = models.CharField(max_length=2,  help_text="country code", null=True)
    country = models.CharField(max_length=200,  help_text="name of conference")

    def __unicode__(self):
         return self.country

class Correspondence(models.Model):
    id = models.AutoField(primary_key=True, help_text="reviewer")
    submission = models.ForeignKey('Submission',on_delete=models.SET_NULL, null=True)
    address1 = models.CharField(max_length=200,  help_text="name of conference")
    address2 = models.CharField(max_length=200,  help_text="name of conference")
    city = models.CharField(max_length=200,  help_text="name of conference")
    state = models.CharField(max_length=200,  help_text="name of conference")
    country = models.ForeignKey('Country',on_delete=models.SET_NULL, null=True)

class Author(models.Model):
    id = models.AutoField(primary_key=True, help_text="reviewer")
    submission = models.ForeignKey('Submission',on_delete=models.SET_NULL, null=True)
    fname = models.CharField(max_length=100,  help_text="name of conference")
    lname = models.CharField(max_length=100,  help_text="name of conference")
    email = models.CharField(max_length=200,  help_text="name of conference")
    organisation = models.CharField(max_length=200,  help_text="name of conference", null=True)
    speaker = models.NullBooleanField(max_length=200,  help_text="speaker", default=True)
