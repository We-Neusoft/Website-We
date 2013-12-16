from django.conf.urls import patterns, url

from file import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    (r'^index.we$', views.index),
    url(r'^(?P<pk>[\w\-]+).we$', views.FileView.as_view(), name='detail'),
    url(r'^(?P<id>[\w\-]+)/download.we$', views.download),
    url(r'^(?P<id>[\w\-]+)/(?P<ip_encoded>[0-9a-f]{8})/download.we$', views.download, name='download'),
)
