from django.conf.urls import patterns, url

from common import views

urlpatterns = patterns('',
    (r'^get_user.we$', views.get_user),
    (r'^qr.we$', views.qr),
)
