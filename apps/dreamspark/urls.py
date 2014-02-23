from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    (r'^index.we$', views.index),
    url(r'^download.we$', views.download, name='download'),
    url(r'^login.we$', views.login, name='login'),
    url(r'^signin.we$', views.signin, name='signin'),
)
