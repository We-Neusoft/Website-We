from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    (r'^index.we$', views.index),
    url(r'^tv.we$', views.tv, name='tv'),
    url(r'^worldcup.we$', views.worldcup, name='worldcup'),
)
