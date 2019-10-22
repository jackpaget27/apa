from django import forms
from .models import *

class PersonForm(forms.Form):
	phonenumber = forms.CharField(required=False)
	dob = forms.CharField(required=False)
	nationality = forms.CharField(required=False)
	address_1 = forms.CharField(required=False)
	address_2 = forms.CharField(required=False)
	address_3 = forms.CharField(required=False)
	address_4 = forms.CharField(required=False)
	home_country = forms.CharField(required=False)
	personal = forms.CharField(required=False)
	facebook = forms.CharField(required=False)
	twitter = forms.CharField(required=False)
	instagram = forms.CharField(required=False)

class EventForm(forms.Form):
	event = forms.CharField(required=False)
	event_location = forms.CharField(required=False)
	team = forms.CharField(required=False)
	year = forms.CharField(required=False)
	position = forms.CharField(required=False)

class ProfileForm(forms.Form):
	profile_text = forms.CharField(widget=forms.Textarea)

class LicenseForm(forms.Form):
	license = forms.FileField(widget=forms.ClearableFileInput())
	expiry_date = forms.CharField(required=False)
	licensetype = forms.CharField(required=False)

class IdentityForm(forms.Form):
	identity = forms.FileField(widget=forms.ClearableFileInput())
	expiry_date = forms.CharField(required=False)
	identitytype = forms.CharField(required=False)