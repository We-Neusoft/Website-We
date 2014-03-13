from django.conf import settings
from django.core.signing import TimestampSigner, BadSignature
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.db.models import Count, Sum
from django.http import Http404, HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.utils.baseconv import base62
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import generic

from datetime import date, datetime, timedelta
from netaddr import IPAddress
from uuid import UUID
from zlib import crc32

from models import File, Download
from backdoors import backdoors
from ip import get_ip
from navigation import get_navbar
from converter import file_size

FILE_ROOT = getattr(settings, 'FILE_ROOT', '/storage/file/')
signer = TimestampSigner()

def index(request):
    result = get_navbar(request)

    unique_files = File.objects.order_by('md5sum', 'sha1sum').distinct('md5sum', 'sha1sum')
    total_sizes = 0
    for unique_file in unique_files:
        total_sizes += unique_file.size

    result.update({
        'file': {
            'total': File.objects.count(),
            'unique': len(unique_files),
            'size': file_size(total_sizes),
        },
        'download': {
            'today': len(Download.objects.filter(time__gte=date.today())),
            'week': len(Download.objects.filter(time__gt=date.today() - timedelta(days=6))),
            'month': len(Download.objects.filter(time__gt=date.today() - timedelta(days=29))),
        },
        'date': {
            'week': date.today() - timedelta(days=6),
            'month': date.today() - timedelta(days=29),
        },
    })

    return render_to_response('file/index.html', result)

class FileView(generic.DetailView):
    model = File

    def get_object(self):
        try:
            id = UUID(bytes=urlsafe_base64_decode(self.kwargs[self.pk_url_kwarg]))
        except ValueError:
            raise Http404
        self.kwargs[self.pk_url_kwarg] = id

        return super(FileView, self).get_object()

    def get_context_data(self, **kwargs):
        context = super(FileView, self).get_context_data(**kwargs)
        context.update(get_navbar(self.request))
        context.update({'key': signer.sign(get_value(self.request, kwargs['object'].id)).replace(':', '')[-33:]})
        context.update({'ip': str(get_ip(self.request))})
        return context

def download(request, id):
    key = request.GET.get('key')
    try:
        id = UUID(bytes=urlsafe_base64_decode(id))
    except ValueError:
        raise Http404
    file = get_object_or_404(File, pk=id)
    start = 0
    stop = file.size - 1

    time = None
    valid = False
    if key:
        time = datetime.fromtimestamp(base62.decode(key[:6]))
        try:
            signer.unsign('%s:%s:%s' % (get_value(request, id), key[:6], key[6:]))
            valid = True
        except BadSignature:
            pass

    if not valid:
        if backdoors.validate_referer(request):
            time = datetime.now().replace(minute=0, second=0, microsecond=0)
        else:
            return redirect(file)

    referer = request.META.get('HTTP_REFERER')

    range = request.META.get('HTTP_RANGE')
    if range:
        start, stop = range.strip('bytes=').split('-')
        if not stop:
            stop = file.size - 1
    else:
        try:
            file.download_set.create(ip=str(get_ip(request)), referer=referer, time=time)
        except IntegrityError:
            pass

    response = StreamingHttpResponse(download_generator(file, int(start), int(stop)), 'application/octet-stream', 200 if not range else 206)
    response['Content-Disposition'] = 'attachment; filename="' + file.name + '"'
    response['Content-Length'] = str(int(stop) - int(start) + 1)
    if range:
        response['Content-Range'] = 'bytes ' + str(start) + '-' + str(stop) + '/' + str(file.size)
    return response

def download_generator(file, start, stop):
    file_path = file.crc32[-2:] + '/' + file.md5sum + file.sha1sum

    with open(FILE_ROOT + file_path, 'rb') as f:
        f.seek(start)
        while True:
            buffer = f.read(65536)
            if buffer:
                yield buffer
            else:
                break

def get_value(request, id):
    return '%s|%s' % (urlsafe_base64_encode(id.bytes), str(get_ip(request)))
