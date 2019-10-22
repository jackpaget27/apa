from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def index(request):
	drivers = Driver.objects.all()

    context = {
    	'drivers' : drivers,
    }
    
    template = loader.get_template('drivers/index.html')
    return HttpResponse(template.render(context, request))