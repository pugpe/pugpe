# -*- coding:utf-8 -*-
from django.core import signing
from django.shortcuts import get_object_or_404, Http404
from django.http import HttpResponse

from events.models import Event

from .models import Attendee
from .generate_cert import generate


def certificate(request, event_slug, slug):
    '''
    Acesado publicamente via link único, afim de adicionar link em
    certificado
    '''
    event = get_object_or_404(Event, slug=event_slug)
    attendee = get_object_or_404(Attendee, slug=slug)

    if attendee.events.filter(pk=event.pk).exists():
        pdf = generate(attendee.name, event)

        response = HttpResponse(mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="certificado.pdf"'
        response.write(pdf.read())
        return response

    return Http404()
