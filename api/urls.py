from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (r'^qrcode/', include('api.qrcode_we.urls', namespace='qrcode')),
)
