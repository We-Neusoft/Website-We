from django.conf.urls import patterns, url

from dreamspark import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    (r'^index.we$', views.index),
    url(r'^download.we$', views.download, name='download'),
)
