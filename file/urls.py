from django.conf.urls import patterns, url

from file import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    (r'^index.we$', views.index),
    url(r'^detail/(?P<pk>[^\.]+).we$', views.FileView.as_view(), name='detail'),
    url(r'^download/(?P<id>[^\.]+).we$', views.download, name='download'),
)
