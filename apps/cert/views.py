# -*- coding:utf-8 -*-
from django.shortcuts import get_object_or_404, Http404
from django.http import HttpResponse

from events.models import Event

from .models import Attendee
from .generate_cert import generate


def certificate(request, slug):
    '''
    Acesado publicamente via link único, afim tornar possível link de
    verificação em certificado
    '''
    attendee = get_object_or_404(Attendee, slug=slug)

    pdf = generate(attendee.name, attendee.event)

    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificado.pdf"'
    response.write(pdf.read())
    return response
