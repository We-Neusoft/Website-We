from django.views import generic

from file.models import File

class FileView(generic.DetailView):
    model = File
