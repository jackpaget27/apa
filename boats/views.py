# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View
from datetime import datetime
from django.urls import reverse
from .forms import *
from .models import *
# Create your views here.

@login_required(login_url='/login/')
def index(request):
	boats = Boat.objects.all()
	context = {
    	'boats' : boats,
	}
	template = loader.get_template('boats/index.html')
	return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def index_engines(request):
	engines = Engine.objects.all()
	context = {
    	'engines' : engines,
	}
	template = loader.get_template('boats/engines_index.html')
	return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def view_engine(request,engine_id):
	engine = Engine.objects.get(id=engine_id)
	services = engine.services.all().order_by('-next_service')
	context = {
		'engine' : engine,
		'services' : services,
	}
	template = loader.get_template('boats/view_engine.html')
	return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def view_boat(request,boat_id):
	boat = Boat.objects.get(id=boat_id)
	services = boat.engine.services.all().order_by('-service_date')
	hull_cols = HullColours.objects.all()
	eng_sers = Engine.objects.all()
	owners = BoatOwners.objects.all()
	form = BoatForm()
	context = {
    	'boat' : boat,
    	'services' : services,
    	'hull_cols' : hull_cols,
		'eng_sers' : eng_sers,
		'owners' : owners,
		'form' : form,
	}
	template = loader.get_template('boats/view.html')
	return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def add_boat(request):
	hull_cols = HullColours.objects.all()
	eng_sers = Engine.objects.all()
	owners = BoatOwners.objects.all()
	form = BoatForm()
	context = {
    	'hull_cols' : hull_cols,
		'eng_sers' : eng_sers,
		'owners' : owners,
		'form' : form,
	}
	template = loader.get_template('boats/addboat.html')
	return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def add_engine(request):
	boats = Boat.objects.all()

	context = {
    	'boats' : boats,
	}
	template = loader.get_template('boats/addengine.html')
	return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def create_engine(request):
	if request.method == "POST":
		form = EngineForm(request.POST)
		if form.is_valid():
			make = form.cleaned_data['make']
			serial_number = form.cleaned_data['serial_number']
			build_year = datetime.strptime(form.cleaned_data['build_date'], "%d/%m/%Y")
			
			engine = Engine(make=make, serial_number=serial_number, build_year=build_year)
			engine.save()
			
			if not form.cleaned_data['current_boat'] == "":
				boat = Boat.objects.get(id=(form.cleaned_data['current_boat'].split("[")[1]).split("]")[0])
				boat.engine = engine
				boat.save()

			return HttpResponseRedirect(reverse('boats:view_engine', kwargs={'engine_id' : engine.id}))

@login_required(login_url='/login/')
def create_boat(request):

	if request.method == "POST":
		form = BoatForm(request.POST)
		if form.is_valid():
			boat =Boat(registration = form.cleaned_data['boat_registration'])
			boat.hull_colour = HullColours.objects.get(id=(form.cleaned_data['hull_colour'].split("[")[1]).split("]")[0])
			boat.boat_owner = BoatOwners.objects.get(id=(form.cleaned_data['owner'].split("[")[1]).split("]")[0])
			boat.engine = Engine.objects.get(id=(form.cleaned_data['engine_serial'].split("[")[1]).split("]")[0])
			boat.build_date = datetime.strptime(form.cleaned_data['build_date'], "%d/%m/%Y")
			if form.cleaned_data['insured'] == "Yes":
				boat.insured = True
				boat.insurance_policy = form.cleaned_data['insurance_policy']
			else:
				boat.insured = False
				boat.insurance_policy = ""
			boat.current_value = form.cleaned_data['current_value']

			boat.save()

	return HttpResponseRedirect(reverse('boats:view_boat', kwargs={'id' : boat.id}))

@login_required(login_url='/login/')
def update_boat(request, boat_id):

	if request.method == "POST":
		form = BoatForm(request.POST)
		boat = Boat.objects.get(id=boat_id)
		if form.is_valid():
			boat.registration = form.cleaned_data['boat_registration']
			boat.hull_colour = HullColours.objects.get(id=(form.cleaned_data['hull_colour'].split("[")[1]).split("]")[0])
			boat.owner = BoatOwners.objects.get(id=(form.cleaned_data['owner'].split("[")[1]).split("]")[0])
			boat.engine = Engine.objects.get(id=(form.cleaned_data['engine_serial'].split("[")[1]).split("]")[0])
			boat.build_date = datetime.strptime(form.cleaned_data['build_date'], "%d/%m/%Y")
			if form.cleaned_data['insured'] == "Yes":
				boat.insured = True
				boat.insurance_policy = form.cleaned_data['insurance_policy']
			else:
				boat.insured = False
				boat.insurance_policy = ""
			boat.current_value = form.cleaned_data['current_value']

			boat.save()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='/login/')
def add_service(request,engine_id):
	engine = Engine.objects.get(id=engine_id)

	if request.method == "POST":
		form = ServiceForm(request.POST)
		if form.is_valid():
			service_date = datetime.strptime(form.cleaned_data['service_date'], "%d/%m/%Y")
			next_service = datetime.strptime(form.cleaned_data['next_service'], "%d/%m/%Y")
			service_notes = form.cleaned_data['service_note']
			service = EngineServices(service_date=service_date,next_service=next_service,notes=service_notes)
			service.save()
			engine.services.add(service)
			engine.save()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))		

@login_required(login_url='/login/')
def update_engine(request,engine_id):

	if request.method == "POST":
		form = EngineForm(request.POST)
		engine = Engine.objects.get(id=engine_id)
		if form.is_valid():
			build_date = datetime.strptime(form.cleaned_data['build_date'], "%d/%m/%Y")
			engine.make = form.cleaned_data['make']
			engine.serial_number = form.cleaned_data['serial_number']
			engine.build_year = build_date
			print(engine.build_year)
			engine.save()
			boat = Boat.objects.get(id=(form.cleaned_data['current_boat'].split("[")[1]).split("]")[0])
			boat.engine = engine
			boat.save()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='/login/')
def upload_boat_image(request, boat_id):
	boat = Boat.objects.get(id=boat_id)
	if request.method == "POST":
		form = PhotoForm(request.POST, request.FILES)
		files = request.FILES.getlist('boat_image')
		if form.is_valid():
			for f in files:
				boat_image = BoatImages(boat_image=f)
				boat_image.save()
				boat.images.add(boat_image)
				boat.save()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='/login/')
def delete_boat_image(request, image_id):
	boat_image = BoatImages.objects.get(id=image_id).delete()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

class BasicUploadView(View):
    def get(self, request):
        photos_list = BoatImages.objects.all()
        return render(self.request, 'photos/basic_upload/index.html', {'photos': photos_list})

    def post(self, request):
		form = PhotoForm(self.request.POST, self.request.FILES)
		files = request.FILES.getlist('boat_image')
		if form.is_valid():
			
			for f in files:
				print(f)
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
		else:
			print(form.errors)
			data = {'is_valid': False}
			return JsonResponse(data)

