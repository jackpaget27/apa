# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from racers.models import *
from boats.models import *

# Create your models here.

class SponsorLogo(models.Model):
	image = models.FileField(upload_to='sponsors/logos')

class SponsorContracts(models.Model):
	name = models.CharField(max_length=250)
	file_contract = models.FileField(upload_to='sponsors/contracts')

	def __unicode__(self):
		return self.name 

class SponsorBenefits(models.Model):
	name = models.CharField(max_length=250)
	value = models.CharField(max_length=250, null=True)

	def __unicode__(self):
		return self.name

class SoponsorshipLevel(models.Model):
	name = models.CharField(max_length=250)
	value = models.CharField(max_length=250)
	benefits = models.ManyToManyField(SponsorBenefits)

	def __unicode__(self):
		return self.name

class SponsorPayments(models.Model):
	amount = models.CharField(max_length=250)
	date = models.DateField(auto_now_add=True)


class Sponsors(models.Model):
	member_link = models.ForeignKey(Members, null=True)
	sponsor_name = models.CharField(max_length=250)
	logo = models.ManyToManyField(SponsorLogo)
	email_address = models.EmailField(max_length=254)
	active_sponsor = models.BooleanField(default=True)
	contract = models.ManyToManyField(SponsorContracts)
	payments = models.ManyToManyField(SponsorPayments)
	driver_sponsor = models.BooleanField(default=False)
	driver_sponsored = models.CharField(max_length=250, null=True)
	boat_sponsored = models.ManyToManyField(Boat)