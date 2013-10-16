from django.conf.urls import patterns, url

from file import views

urlpatterns = patterns('',
    url(r'^(?P<pk>[^\.]+).we$', views.FileView.as_view(), name='file'),
)
