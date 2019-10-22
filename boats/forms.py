from django import forms
from .models import *

class PhotoForm(forms.Form):
	boat_image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class BoatForm(forms.Form):
	boat_registration = forms.CharField(required=False)
	hull_colour = forms.CharField(required=False)
	owner = forms.CharField(required=False)
	current_value = forms.CharField(required=False)
	insured = forms.CharField(required=False)
	insurance_policy = forms.CharField(required=False)
	engine_serial = forms.CharField(required=False)
	build_date = forms.CharField(required=False)
	
class EngineForm(forms.Form):
	make = forms.CharField(required=False)
	serial_number = forms.CharField(required=False)
	build_date = forms.CharField(required=False)
	current_boat = forms.CharField(required=False)

class ServiceForm(forms.Form):
	service_date = forms.CharField(required=False)
	next_service = forms.CharField(required=False)
	service_note = forms.CharField(widget=forms.Textarea, required=False)