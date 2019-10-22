from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from . import views
app_name = 'sponsors'
urlpatterns = [
	url(r'add/$', views.add_sponsor, name='add_sponsor'),
    url('', views.index, name='index'),
]