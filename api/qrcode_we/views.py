from django.http import HttpResponse

import qrcode

def qr(request, size):
    if int(size) < 1:
        size = 1
    if int(size) > 32:
        size = 32

    qr = qrcode.QRCode(box_size=size, border=2)
    qr.add_data(request.META.get('HTTP_REFERER'))
    qr_image = qr.make_image()
    response = HttpResponse(content_type='image/png')
    qr_image.save(response, 'PNG')
    return response
