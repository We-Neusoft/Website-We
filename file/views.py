from django.conf import settings
from django.http import StreamingHttpResponse
from django.views import generic

from file.models import File, Download

DEBUG_ENABLED = getattr(settings, 'DEBUG', True)

class FileView(generic.DetailView):
    model = File

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

    response = StreamingHttpResponse(download_generator(file, int(start), int(stop), ip, referer), file.mime, 200 if not range else 206)
    response['Content-Disposition'] = 'attachment; filename="' + file.name + '"'
    response['Content-Length'] = str(int(stop) - int(start) + 1)
    if range:
        response['Content-Range'] = 'bytes ' + str(start) + '-' + str(stop) + '/' + str(file.size)
    return response

def download_generator(file, start, stop, ip, referer):
    file_path = file.crc32[-2:] + '/' + file.md5sum + file.sha1sum

    with open('/storage/file/' + file_path, 'rb') as f:
        f.seek(start)
        while True:
            buffer = f.read(4096)
            if buffer:
                yield buffer
            else:
                break;
