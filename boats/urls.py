from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from . import views
app_name = 'boats'
urlpatterns = [
	url(r'^boat/(?P<boat_id>[0-9]+)/$', views.view_boat, name='view_boat'),
	url(r'^engine/(?P<engine_id>[0-9]+)/$', views.view_engine, name='view_engine'),
	url(r'^uploadboatimage/(?P<boat_id>[0-9]+)/$', views.upload_boat_image, name='upload_boat_image'),
	url(r'^updateboat/(?P<boat_id>[0-9]+)/$', views.update_boat, name='update_boat'),
	url(r'^updateengine/(?P<engine_id>[0-9]+)/$', views.update_engine, name='update_engine'),
	url(r'^engineservice/(?P<engine_id>[0-9]+)/$', views.add_service, name='update_service'),
	url(r'^deleteboatimage/(?P<image_id>[0-9]+)/$', views.delete_boat_image, name='delete_boat_image'),
	url(r'^addboat/$', views.add_boat, name='add_boat'),
	url(r'^addengine/$', views.add_engine, name='add_engine'),
	url(r'^createboat/$', views.create_boat, name='create_boat'),
	url(r'^createengine/$', views.create_engine, name='create_engine'),
	url(r'^engines/$', views.index_engines, name='engines_index'),
    url('', views.index, name='index'),
]