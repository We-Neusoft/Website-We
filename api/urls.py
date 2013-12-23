from django.conf.urls import patterns, url

from api import views

urlpatterns = patterns('',
    url(r'^qr/small.we$', views.qr, {'size': 2, 'border': 1}, name='qr_small'),
    url(r'^qr/middle.we$', views.qr, {'size': 4, 'border': 2}, name='qr_middle'),
    url(r'^qr/large.we$', views.qr, {'size': 8, 'border': 3}, name='qr_large'),
    url(r'^qr/xlarge.we$', views.qr, {'size': 16, 'border': 4}, name='qr_xlarge'),
)
