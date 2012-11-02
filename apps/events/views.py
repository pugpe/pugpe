# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

import datetime
from django.utils.timezone import utc

from .models import Event, EventTalk
from .models import Support, Sponsor


class EventMixin(object):
    '''Add event to context of views that require an event'''
    def get_context_data(self, **kwargs):
        event = get_object_or_404(Event, slug=self.kwargs['event_slug'])
        sponsors = Sponsor.objects.filter(event=event)
        supporters = Support.objects.filter(event=event)

        now = datetime.datetime.utcnow().replace(tzinfo=utc)

        allow_submission = False
        if event.submission_deadline > now:
            allow_submission = True

        kwargs.update(
            {'event': event, 'sponsors': sponsors, 'supporters': supporters,
            'allow_submission': allow_submission, },
        )

        return super(EventMixin, self).get_context_data(**kwargs)


class TalkListView(EventMixin, ListView):
    model = EventTalk
    template_name = u'events/event.html'
    context_object_name = 'talks'

    def get_queryset(self):
        qs = EventTalk.active.filter(event__slug=self.kwargs['event_slug'])
        return qs.order_by('start')


class PastEvents(ListView):
    template_name = 'events/past_events.html'
    model = Event
    context_object_name = 'events'
