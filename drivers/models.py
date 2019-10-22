from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

#
# Racing Licenses
# 

class RacingLicenseTypes(models.Model):
	name = models.CharField(max_length=250)

	def __unicode__(self):
		return self.name 

class RacingLicenseScans(models.Model):
	file = models.FileField(upload_to='media/licenses')
	expires = models.DateField()
	uploaded_date = models.DateTimeField(auto_now_add=True)

#
# Identity Documents
#

class IdentityTypes(models.Model):
	name = models.CharField(max_length=250)

	def __unicode__(self):
		return self.name 

class IdentityScans(models.Model):
	file = models.FileField(upload_to='media/identity')
	expires = models.DateField()
	uploaded_date = models.DateTimeField(auto_now_add=True)
	identity_type = models.ForeignKey(IdentityTypes)

#
# Driver Profile Images
#

class DriverProfile(models.Model):
	file = models.FileField(upload_to='media/profile')
	expires = models.DateField()
	uploaded_date = models.DateTimeField(auto_now_add=True)
	profile_image = models.BooleanField(default=False)

class CareerVictory(models.Model):
	name = models.CharField(max_length=250)
	location = CountryField(null=True)
	team = models.CharField(max_length=250, null=True)
	year = models.CharField(max_length=250)
	position = models.CharField(max_length=2)

#
# Drivers Main Model
#

