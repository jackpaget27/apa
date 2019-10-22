from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View
from datetime import datetime
from django.urls import reverse
from django_countries.fields import Country, countries

from .models import *
from .forms import *
from boats.forms import PhotoForm
# Create your views here.

def check_user(request, id):
	member = Members.objects.get(id=id)
	if request.user.id == member.username.id:
		return True
	elif user.is_staff == True:
		return True
	else:
		return False

@login_required(login_url='/login/')
def index(request):
	racers = Members.objects.filter(racer=True)
	context = {
    	'racers' : racers,
	}
	template = loader.get_template('racers/index.html')
	return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def user_profile(request, racer_id):
	cu = check_user(request, racer_id)

	racer = Members.objects.get(id=racer_id)
	victories = racer.career_victories.all().order_by("-year")
	licenses = RacingLicenseTypes.objects.all()
	identities = IdentityTypes.objects.all()
	racer_licenses = racer.licenses.all().order_by("-expires")
	racer_identities = racer.identity.all().order_by("-expires")
	context = {
    	'racer' : racer,
    	'countries' : countries,
    	'victories' : victories,
    	'licenses' : licenses,
    	'racer_licenses' : racer_licenses,
    	'identities' : identities,
    	'racer_identities' : racer_identities,
	}

	if cu == False:
		template = loader.get_template('racers/profile_santized.html')
	else:
		template = loader.get_template('racers/profile.html')

	return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def add_license(request, racer_id):
	cu = check_user(request, racer_id)
	if cu == False:
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

	racer = Members.objects.get(id=racer_id)

	if request.method == "POST":
		form = LicenseForm(request.POST,request.FILES)
		scan = request.FILES.get('license')
		if form.is_valid():
			r_l = RacingLicenseScans(file=scan)
			r_l.expires = datetime.strptime(form.cleaned_data['expiry_date'], "%d/%m/%Y")
			lic_type = RacingLicenseTypes.objects.get(id=form.cleaned_data['licensetype'].split("[")[1].split("]")[0])
			r_l.license_type = lic_type
			r_l.save()
			racer.licenses.add(r_l)
			racer.save()
	
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='/login/')
def add_identity(request, racer_id):
	cu = check_user(request, racer_id)
	if cu == False:
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

	racer = Members.objects.get(id=racer_id)

	if request.method == "POST":
		form = IdentityForm(request.POST,request.FILES)
		scan = request.FILES.get('identity')
		print(form.errors)
		if form.is_valid():
			r_l = IdentityScans(file=scan)
			r_l.expires = datetime.strptime(form.cleaned_data['expiry_date'], "%d/%m/%Y")
			lic_type = IdentityTypes.objects.get(id=form.cleaned_data['identitytype'].split("[")[1].split("]")[0])
			r_l.identity_type = lic_type
			r_l.save()
			racer.identity.add(r_l)
			racer.save()
	
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='/login/')
def add_victory(request, racer_id):
	cu = check_user(request, racer_id)
	if cu == False:
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

	racer = Members.objects.get(id=racer_id)
	if request.method == "POST":
		form = EventForm(request.POST)
		if form.is_valid():
			victory = CareerVictory(name=form.cleaned_data['event'])
			victory.location = form.cleaned_data['event_location'].split("[")[1].split("]")[0]
			victory.team = form.cleaned_data['team']
			victory.year = form.cleaned_data['year']
			victory.position = form.cleaned_data['position']
			victory.save()
			racer.career_victories.add(victory)
			racer.save()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url='/login/')
def profile_text(request, racer_id):
	cu = check_user(request, racer_id)
	if cu == False:
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

	racer = Members.objects.get(id=racer_id)
	if request.method == "POST":
		form = ProfileForm(request.POST)
		if form.is_valid():
			racer.profile_text = form.cleaned_data['profile_text']
			racer.save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))		

@login_required(login_url='/login/')
def profile_update(request, racer_id):
	cu = check_user(request, racer_id)
	if cu == False:
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

	racer = Members.objects.get(id=racer_id)
	if request.method == "POST":
		form = PersonForm(request.POST)
		print(form.errors)
		if form.is_valid():
			phonenumber = form.cleaned_data['phonenumber']
			dob = form.cleaned_data['dob']
			nationality = form.cleaned_data['nationality']
			address_1 = form.cleaned_data['address_1']
			address_2 = form.cleaned_data['address_2']
			address_3 = form.cleaned_data['address_3']
			address_4 = form.cleaned_data['address_4']
			home_country = form.cleaned_data['home_country']
			personal = form.cleaned_data['personal']
			twitter  = form.cleaned_data['twitter']
			instagram  = form.cleaned_data['instagram']
			facebook  = form.cleaned_data['facebook']

			racer.date_of_birth = datetime.strptime(dob, '%d/%m/%Y')
			racer.telephone_number = phonenumber
			racer.address_line_1 = address_1
			racer.address_line_2 = address_2
			racer.address_line_3 = address_3
			racer.address_line_4 = address_4
			racer.address_country = home_country.split("[")[1].split("]")[0]
			racer.country = nationality.split("[")[1].split("]")[0]
			racer.facebook_handle = facebook
			racer.insta_handle = instagram
			racer.twitter_handle = twitter
			racer.personal_site = personal
			racer.save()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='/login/')
def upload_profile_image(request, person_id):
	cu = check_user(request, racer_id)
	if cu == False:
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

	person = Members.objects.get(id=person_id)
	if request.method == "POST":
		form = PhotoForm(request.POST, request.FILES)
		files = request.FILES.getlist('boat_image')
		if form.is_valid():
			for f in files:
				boat_image = DriverProfile(file=f)
				boat_image.save()
				person.profile_images.add(boat_image)
				person.save()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='/login/')
def delete_profile_image(request, image_id):
	cu = check_user(request, racer_id)
	if cu == False:
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
	person_image = DriverProfile.objects.get(id=image_id).delete()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))