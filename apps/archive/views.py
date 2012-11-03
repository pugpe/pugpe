# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.utils import timezone

from events.models import Event


class PastEvents(ListView):
    template_name = 'archive/past_events.html'
    model = Event
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(date__lt=timezone.now).order_by('-date')
