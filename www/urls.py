from django.conf.urls import patterns

urlpatterns = patterns('',
    (r'^$', 'www.views.index'),
    (r'^index.we$', 'www.views.index'),
    (r'^more_services.we$', 'www.views.more_services'),
)
