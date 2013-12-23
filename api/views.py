from django.http import HttpResponse

import qrcode

def qr(request, size, border):
    qr = qrcode.QRCode(box_size=size, border=border)
    qr.add_data(request.META.get('HTTP_REFERER'))
    qr_image = qr.make_image()
    response = HttpResponse(content_type='image/png')
    qr_image.save(response, 'PNG')
    return response
