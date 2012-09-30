# -*- coding: utf-8 -*-
from django.views.generic import ListView

from .models import Event, EventTalk


class TalkListView(ListView):
    model = EventTalk
    template_name = u'events/event.html'
    context_object_name = 'talks'

    def get_queryset(self):
        return EventTalk.active.filter(event__slug=self.kwargs['event_slug'])

    def get_context_data(self, **kwargs):
        event = Event.objects.get(slug=self.kwargs['event_slug'])

        kwargs.update({'event': event})
        return super(TalkListView, self).get_context_data(**kwargs)
