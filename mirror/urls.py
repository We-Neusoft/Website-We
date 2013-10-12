from django.conf.urls import patterns, url

from mirror import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    (r'^index.we$', views.index),
    url(r'^configurations.we$', views.configurations, name='configurations'),
)
