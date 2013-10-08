from django.conf.urls import patterns, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'we.views.home', name='home'),
    # url(r'^we/', include('we.foo.urls')),
    (r'', include('www.urls')),
    (r'^www/', include('www.urls')),
    (r'^mirror/', include('mirror.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)