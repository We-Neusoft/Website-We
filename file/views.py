from django.http import StreamingHttpResponse
from django.views import generic

from file.models import File

class FileView(generic.DetailView):
    model = File

def download(request, id):
    return StreamingHttpResponse(id, content_type='application/octet-stream')
