from django.conf.urls import patterns, url

from api.qrcode_we import views

urlpatterns = patterns('',
    url(r'^small.we$', views.qr, {'size': 2}, name='small'),
    url(r'^middle.we$', views.qr, {'size': 4}, name='middle'),
    url(r'^large.we$', views.qr, {'size': 8}, name='large'),
    (r'^(?P<size>\d+).we$', views.qr),
)
