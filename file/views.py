from django.conf import settings
from django.db.models import Count, Sum
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render_to_response
from django.views import generic

from datetime import date, timedelta

from file.models import File, Download
from we.utils.unit import file_size

DEBUG_ENABLED = getattr(settings, 'DEBUG', True)
FILE_ROOT = getattr(settings, 'FILE_ROOT', '/storage/file/')

result = {'nav_file': 'active'}

def index(request):
    unique_files = File.objects.order_by('md5sum', 'sha1sum').distinct('md5sum', 'sha1sum')
    total_sizes = 0
    for unique_file in unique_files:
        total_sizes += unique_file.size

    file = dict()
    file['total'] = File.objects.count()
    file['unique'] = len(unique_files)
    file['size'] = file_size(total_sizes)

    result['file'] = file

    download = dict()
    download['today'] = len(Download.objects.filter(time__gte=date.today()))
    download['week'] = len(Download.objects.filter(time__gt=date.today() - timedelta(days=6)))
    download['total'] = Download.objects.count()

    result['download'] = download

    return render_to_response('file/index.html', result)

class FileView(generic.DetailView):
    model = File

    def get_context_data(self, **kwargs):
        context = super(FileView, self).get_context_data(**kwargs)
        context['nav_file'] = 'active'
        return context

def download(request, id):
    file = File.objects.get(pk=id)
    start = 0
    stop = file.size - 1

    if DEBUG_ENABLED:
        ip = request.META['HTTP_X_REAL_IP']
    else:
        ip = request.META['REMOTE_ADDR']

    referer = request.META.get('HTTP_REFERER')

    range = request.META.get('HTTP_RANGE')
    if range:
        start, stop = range.strip('bytes=').split('-')
        if not stop:
            stop = file.size - 1
    else:
        file.download_set.create(ip=ip, referer=referer)

    response = StreamingHttpResponse(download_generator(file, int(start), int(stop), ip, referer), 'application/octet-stream', 200 if not range else 206)
    response['Content-Disposition'] = 'attachment; filename="' + file.name + '"'
    response['Content-Length'] = str(int(stop) - int(start) + 1)
    if range:
        response['Content-Range'] = 'bytes ' + str(start) + '-' + str(stop) + '/' + str(file.size)
    return response

def download_generator(file, start, stop, ip, referer):
    file_path = file.crc32[-2:] + '/' + file.md5sum + file.sha1sum

    with open(FILE_ROOT + file_path, 'rb') as f:
        f.seek(start)
        while True:
            buffer = f.read(4096)
            if buffer:
                yield buffer
            else:
                break
