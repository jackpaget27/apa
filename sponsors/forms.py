from django import forms
from .models import *

class SponsorForm(forms.Form):
	phonenumber = forms.CharField(required=False)
	sponsor_name = forms.CharField(required=False)
	logo = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}))
	email_address = forms.CharField(required=False)
	address_1 = forms.CharField(required=False)
	address_2 = forms.CharField(required=False)
	address_3 = forms.CharField(required=False)
	address_4 = forms.CharField(required=False)
	country = forms.CharField(required=False)
	phonenumber = forms.CharField(required=False)
	profile_text = forms.CharField(widget=forms.Textarea(), required=False)
	facebook = forms.CharField(required=False)
	twitter = forms.CharField(required=False)
	instagram = forms.CharField(required=False)
	website = forms.CharField(required=False)
