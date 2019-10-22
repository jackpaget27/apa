from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from . import views
app_name = 'racers'
urlpatterns = [
	url(r'^racer/(?P<racer_id>[0-9]+)/$', views.user_profile, name='view_user'),
	url(r'^uploadracerimage/(?P<person_id>[0-9]+)/$', views.upload_profile_image, name='upload_profile_image'),
	url(r'^updateprofile/(?P<racer_id>[0-9]+)/$', views.profile_update, name='profile_update'),
	url(r'^addvictory/(?P<racer_id>[0-9]+)/$', views.add_victory, name='add_victory'),
	url(r'^profiletext/(?P<racer_id>[0-9]+)/$', views.profile_text, name='profile_text'),
	url(r'^addlicense/(?P<racer_id>[0-9]+)/$', views.add_license, name='add_license'),
	url(r'^addidentity/(?P<racer_id>[0-9]+)/$', views.add_identity, name='add_identity'),
	url(r'^deleteprofileimage/(?P<image_id>[0-9]+)/$', views.delete_profile_image, name='delete_profile_image'),
    url('', views.index, name='index'),
]