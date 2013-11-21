from django.conf.urls import patterns, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'we.views.home', name='home'),
    # url(r'^we/', include('we.foo.urls')),
    (r'^([^/]+/)?common/', include('common.urls')),
    (r'^www/', include('www.urls', namespace='www')),
    (r'^mirror/', include('mirror.urls', namespace='mirror')),
    (r'^dreamspark/', include('dreamspark.urls', namespace='dreamspark')),
    (r'^file/', include('file.urls', namespace='file')),
    (r'^me/', include('me.urls', namespace='me')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
