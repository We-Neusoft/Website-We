from django.conf.urls import patterns, url

from file import views

urlpatterns = patterns('',
    url(r'^file/(?P<pk>[^\.]+).we$', views.FileView.as_view(), name='file'),
    url(r'^download/(?P<id>[^\.]+).we$', views.download, name='download'),
)
