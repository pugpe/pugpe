# -*- coding: utf-8 -*-
from django.views.generic import ListView

from .models import Event, EventTalk
from .models import Support, Sponsor


class EventMixin(object):
    '''Add event to context of views that require an event'''
    def get_context_data(self, **kwargs):
        event = Event.objects.get(slug=self.kwargs['event_slug'])
        sponsors = Support.objects.filter(event=event)
        supporters = Support.objects.filter(event=event)

        kwargs.update(
            {'event': event, 'sponsors': sponsors, 'supporters': supporters},
        )
        return super(EventMixin, self).get_context_data(**kwargs)


class TalkListView(EventMixin, ListView):
    model = EventTalk
    template_name = u'events/event.html'
    context_object_name = 'talks'

    def get_queryset(self):
        return EventTalk.active.filter(event__slug=self.kwargs['event_slug'])
