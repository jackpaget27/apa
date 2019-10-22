# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

#
# Engine Information
#

class EngineServices(models.Model):
	service_date = models.DateField()
	next_service = models.DateField()
	notes = models.TextField(null=True)

class Engine(models.Model):
	serial_number  = models.CharField(max_length=250)
	build_year = models.DateField()
	services = models.ManyToManyField(EngineServices)
	make = models.CharField(max_length=250,null=True)

	def next_service(self):
		try:
			service_date = (self.services.all().order_by('-next_service')[0]).next_service
		except:
			service_date = datetime.now()

		return service_date

	def current_boat(self):
		try:
			boat = self.boat_set.all()[0]
		except:
			boat = None
		return boat

	def service_nat(self):
		exp_dt = datetime.strptime((self.next_service()).strftime('%Y-%m-%d'), '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%f')
		exp_dt = datetime.strptime(exp_dt, '%Y-%m-%dT%H:%M:%S.%f')
		return exp_dt

#
# Boat
#

class BoatImages(models.Model):
	boat_image = models.FileField(upload_to='boats')
	profile_image = models.BooleanField(default=False)
	caption = models.TextField(null=True)
	title = models.CharField(max_length=250,null=True)

	def __unicode__(self):
		return self.title

class HullColours(models.Model):
	colour = models.CharField(max_length=250)

	def __unicode__(self):
		return self.colour

class BoatOwners(models.Model):
	company_name = models.CharField(max_length=250, null=True)
	person_name = models.ForeignKey(User, null=True)

	def display_name(self):
		if self.company_name:
			return self.company_name
		else:
			return ' '.join([self.person_name.first_name, self.person_name.last_name])


class Boat(models.Model):
	registration = models.CharField(max_length=250, null=True)
	hull_colour = models.ForeignKey(HullColours, null=True)
	owner = models.ForeignKey(BoatOwners, null=True)
	replacement_value = models.CharField(max_length=250, null=True)
	insured = models.BooleanField(default=False)
	insurance_policy = models.CharField(max_length=250, null=True)
	engine = models.ForeignKey(Engine, null=True)
	images = models.ManyToManyField(BoatImages)
	build_date = models.DateField(null=True)

	def insurance_display(self):
		if self.insured == True:
			return ' '.join(['Insured', self.insurance_policy])
		else:
			return 'Uninsured'

	def profile_image(self):
		try:
			profile_image = ((self.images.filter(profile_image=True))[0]).boat_image
		except:
			profile_image = ""

		return profile_image

