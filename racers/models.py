from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from dateutil.relativedelta import relativedelta
# Create your models here.

#
# Racing Licenses
# 

class RacingLicenseTypes(models.Model):
	name = models.CharField(max_length=250)

	def __unicode__(self):
		return self.name 

class RacingLicenseScans(models.Model):
	file = models.FileField(upload_to='licenses')
	expires = models.DateField()
	uploaded_date = models.DateTimeField(auto_now_add=True)
	license_type = models.ForeignKey(RacingLicenseTypes, null=True)

	def expiry_dt(self):
		exp_dt = datetime.strptime((self.expires).strftime('%Y-%m-%d'), '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%f')
		exp_dt = datetime.strptime(exp_dt, '%Y-%m-%dT%H:%M:%S.%f')
		return exp_dt
#
# Identity Documents
#

class IdentityTypes(models.Model):
	name = models.CharField(max_length=250)

	def __unicode__(self):
		return self.name 

class IdentityScans(models.Model):
	file = models.FileField(upload_to='identity')
	expires = models.DateField()
	uploaded_date = models.DateTimeField(auto_now_add=True)
	identity_type = models.ForeignKey(IdentityTypes)

	def expiry_dt(self):
		exp_dt = datetime.strptime((self.expires).strftime('%Y-%m-%d'), '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%f')
		exp_dt = datetime.strptime(exp_dt, '%Y-%m-%dT%H:%M:%S.%f')
		return exp_dt

#
# Driver Profile Images
#

class DriverProfile(models.Model):
	file = models.FileField(upload_to='profile')
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

class Members(models.Model):
	username = models.ForeignKey(User, null=True)
	country = CountryField()
	license_types = models.ManyToManyField(RacingLicenseTypes)
	licenses = models.ManyToManyField(RacingLicenseScans)
	identity = models.ManyToManyField(IdentityScans)
	facebook_handle = models.CharField(max_length=250, null=True, blank=True)
	twitter_handle = models.CharField(max_length=250, null=True, blank=True)
	insta_handle = models.CharField(max_length=250, null=True, blank=True)
	personal_site = models.CharField(max_length=250, null=True, blank=True)
	profile_images = models.ManyToManyField(DriverProfile)
	profile_text = models.TextField(null=True, blank=True)
	email_address = models.EmailField(max_length=254)
	telephone_number = PhoneNumberField(null=True)
	address_line_1 = models.CharField(max_length=250)
	address_line_2 = models.CharField(max_length=250, null=True, blank=True)
	address_line_3 = models.CharField(max_length=250, null=True, blank=True)
	address_line_4 = models.CharField(max_length=250, null=True, blank=True)
	address_country = CountryField(null=True)
	years_experience = models.IntegerField(null=True)
	career_victories = models.ManyToManyField(CareerVictory)
	registered_date = models.DateTimeField(auto_now_add=True)
	terms_conditions = models.BooleanField(default=False)
	terms_conditions_date = models.DateTimeField(auto_now_add=True)
	racer = models.BooleanField(default=False)
	sponsor = models.BooleanField(default=False)
	date_of_birth = models.DateField(null=True)
	supplier = models.BooleanField(default=False)
	email_address = models.CharField(max_length=250, null=True)
	active = models.BooleanField(default=False)

	def profile_image(self):
		profile = self.profile_images.filter(profile_image=True)[0]
		return profile.file

	def get_current_age(self):
		age = relativedelta(datetime.now().date(), self.date_of_birth).years
		return age


