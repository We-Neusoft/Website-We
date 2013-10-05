# Create your views here.
from django.shortcuts import render_to_response

def index(request):
   return render_to_response('www/index.weml', {'nav_www': 'active'});

def more_services(request):
   return render_to_response('www/more_services.weml', {'nav_www': 'active'});
