from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'we.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^([^/]+/)?common/', include('common.urls')),
    (r'^www/', include('www.urls', namespace='www')),
    (r'^mirror/', include('mirror.urls', namespace='mirror')),
    (r'^dreamspark/', include('dreamspark.urls', namespace='dreamspark')),
    (r'^file/', include('file.urls', namespace='file')),
    (r'^open/', include('open.urls', namespace='open')),

    (r'^api/', include('api.urls', namespace='api')),
    (r'^me/', include('me.urls', namespace='me')),

    (r'^admin/', include(admin.site.urls)),
)
