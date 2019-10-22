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
from django_countries.fields import Country, countries
from .forms import *
from .models import *
from racers.models import *

# Create your views here.
@login_required(login_url='/login/')
def index(request):

	context = {

	}
	template = loader.get_template('sponsors/index.html')
	return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def add_sponsor(request):

	context = {
		'countries' : countries,

	}
	template = loader.get_template('sponsors/addsponsor.html')
	return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def new_sponsor(request):
	if request.method == "POST":
		form = SponsorForm(request.POST, request.FILES)
		file = request.POST.get('logo')
		if form.is_valid():
			new_sponsor = Sponsors(sponsor_name = form.cleaned_data['sponsor_name'])
			new_sponsor.logo = file
			new_sponsor.email_address = form.cleaned_data['email']
			new_member = Members(address_line_1=form.cleaned_data['address_1'])
			new_member.address_2 = form.cleaned_data['address_2']
			new_member.address_3 = form.cleaned_data['address_3']
			new_member.address_4 = form.cleaned_data['address_4']
			new_member.country = form.cleaned_data['country'].split("[")[1].split("]")[0]
			new_member.address_country = form.cleaned_data['country'].split("[")[1].split("]")[0]
			new_member.telephone_number = form.cleaned_data['phonenumber']
			new_member.sponsor = True
			new_member.profile_text = form.cleaned_data['profile_text']
			new_member.facebook_handle = form.cleaned_data['facebook']
			new_member.twitter_handle = form.cleaned_data['twitter']
			new_member.insta_handle = form.cleaned_data['instagram']
			new_member.personal_site = form.cleaned_data['website']
			new_member.save()
			new_sponsor.member_link = new_member
			new_sponsor.save()
			
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


