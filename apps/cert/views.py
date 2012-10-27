# -*- coding:utf-8 -*-
from django.core import signing
from django.shortcuts import get_object_or_404, Http404
from django.http import HttpResponse

from events.models import Event

from .models import Attendee
from .generate_cert import generate


def certificate(request, token):
    '''
    Acesado publicamente via link único, afim de adicionar link em
    certificado

    token: signing.dumps({'event_pk': n, 'attendee_pk': n})
    '''
    data = signing.loads(token)

    event = get_object_or_404(Event, pk=data.get('event_pk'))
    attendee = get_object_or_404(Attendee, pk=data.get('attendee_pk'))

    if attendee.events.filter(pk=event.pk).exists():
        pdf = generate(attendee.name, event)

        response = HttpResponse(mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="certificado.pdf"'
        response.write(pdf.read())
        return response

    return Http404()
