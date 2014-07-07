from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    (r'^index.we$', views.index),
    url(r'^(?P<pk>[\w\-]+).we$', views.FileView.as_view(), name='detail'),
    url(r'^(?P<id>[\w\-]+)/download.we$', views.download, name='download'),
    url(r'^(?P<pk>[\w\-]+)/play.we$', views.PlayView.as_view(), name='play'),
)
