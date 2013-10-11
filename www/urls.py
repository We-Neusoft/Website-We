from django.conf.urls import patterns, url

from www import views

urlpatterns = patterns('',
    (r'^$', views.index),
    (r'^index.we$', views.index),
    url(r'^more_services.we$', views.more_services, name='more_services'),
)
