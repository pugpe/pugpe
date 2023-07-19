from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from django.http import HttpResponse

from events.models import Event


def index(request):
    ev = Event.objects.filter(index=True).order_by('-id')
    if ev.exists():
        return redirect(
            reverse('events:event', kwargs={'event_slug': ev[0].slug}),
        )
    else:
        return render(request, 'index.html', {})


def health(request):
    return HttpResponse('OK')