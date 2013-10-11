from django.conf.urls import patterns, url

urlpatterns = patterns('',
    (r'^$', 'mirror.views.index'),
    (r'^index.we$', 'mirror.views.index'),
    url(r'^configurations.we$', 'mirror.views.configurations', name='configurations'),
)
