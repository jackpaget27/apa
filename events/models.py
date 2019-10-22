# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from sponsors.models import *
from boats.models import *
from drivers.models import *

# Create your models here.

#
# Hosts
#

class EventHosts(models.Model):
	email_address = models.EmailField(max_length=254)
	telephone_number = PhoneNumberField(null=True)
	address_line_1 = models.CharField(max_length=250)
	address_line_2 = models.CharField(max_length=250, null=True, blank=True)
	address_line_3 = models.CharField(max_length=250, null=True, blank=True)
	address_line_4 = models.CharField(max_length=250, null=True, blank=True)
	address_country = CountryField(null=True)
	hosting_cost = models.CharField(max_length=250, null=True)

#
# Suppliers
#

class SupplierContracts(models.Model):
	contract = models.FileField(upload_to='media/supplier/contracts')
	contract_value = models.CharField(max_length=250)
	contract_paid = models.DateField()

class SupplierTypes(models.Model):
	name = models.CharField(max_length=250)

	def __unicode__(self):
		return self.name

class EventSupplier(models.Model):
	supplier_class = models.ManyToManyField(SupplierTypes)
	email_address = models.EmailField(max_length=254)
	telephone_number = PhoneNumberField(null=True)
	address_line_1 = models.CharField(max_length=250)
	address_line_2 = models.CharField(max_length=250, null=True, blank=True)
	address_line_3 = models.CharField(max_length=250, null=True, blank=True)
	address_line_4 = models.CharField(max_length=250, null=True, blank=True)
	address_country = CountryField(null=True)
	supplier_contracts = models.ManyToManyField(SupplierContracts)

#
# Event
#

class RaceDrivers(models.Model):
	#driver = models.ForeignKey(Driver)
	boat = models.ForeignKey(Boat)

class Lap(models.Model):
	competitor = models.ForeignKey(RaceDrivers)
	time = models.IntegerField()

class Races(models.Model):
	heat = models.CharField(max_length=250)
	race_date_time = models.DateTimeField(null=True)
	event_competitors = models.ManyToManyField(RaceDrivers)
	event_result = models.ManyToManyField(Lap)

class Event(models.Model):
	city = models.CharField(max_length=250)
	country = CountryField()
	start_date = models.DateField()
	end_date = models.DateField()
	host = models.ManyToManyField(EventHosts)
	#drivers = models.ManyToManyField(Driver)
	races = models.ManyToManyField(Races)
	sponsors = models.ManyToManyField(Sponsors)
	supplier_contracts = models.ManyToManyField(SupplierContracts)

class DriverEventPoints(models.Model):
	event = models.ForeignKey(Event)
	#driver = models.ForeignKey(Driver)
	points = models.IntegerField()

#
# Championship
#

class Championship(models.Model):
	name = models.CharField(max_length=250)
	events = models.ManyToManyField(Event)




