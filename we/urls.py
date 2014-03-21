from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'we.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^([^/]+/)?common/', include('common.urls')),
    (r'^www/', include('apps.www.urls', namespace='www')),
    (r'^mirror/', include('apps.mirror.urls', namespace='mirror')),
    (r'^dreamspark/', include('apps.dreamspark.urls', namespace='dreamspark')),
    (r'^file/', include('apps.file.urls', namespace='file')),
    (r'^open/', include('apps.open.urls', namespace='open')),

    (r'^me/', include('apps.me.urls', namespace='me')),

    (r'^admin/', include(admin.site.urls)),
)

handler404 = 'we.views.http_404_view'
handler500 = 'we.views.http_500_view'
