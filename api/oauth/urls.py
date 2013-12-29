from django.conf.urls import patterns, url

from api.oauth import views

urlpatterns = patterns('',
    url(r'^authorize.we$', views.authorize, name='authorize'),
)
