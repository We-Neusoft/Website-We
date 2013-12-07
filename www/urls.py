from django.conf.urls import patterns, url

from www import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    (r'^index.we$', views.index),
    url(r'^more_services.we$', views.MoreServicesView.as_view(), name='more_services'),
)
