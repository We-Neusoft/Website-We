from django.conf.urls import patterns

urlpatterns = patterns('',
    (r'^$', 'mirror.views.index'),
    (r'^index.we$', 'mirror.views.index'),
    (r'^configurations.we$', 'mirror.views.configurations'),
)
