# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect

from .models import Event, EventTalk
from .models import Support, Sponsor

from core.views import SimpleTemplateView


class EventMixin(object):
    '''Add event to context of views that require an event'''
    event = None
    sponsors = None
    supporters = None

    def dispatch(self, request, *args, **kwargs):
        self.event = get_object_or_404(Event, slug=kwargs['event_slug'])
        self.sponsors = Sponsor.objects.filter(event=self.event)
        self.supporters = Support.objects.filter(event=self.event)

        return super(EventMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs.update({
            'event': self.event,
            'sponsors': self.sponsors,
            'supporters': self.supporters,
        })

        return super(EventMixin, self).get_context_data(**kwargs)


class TalkListView(EventMixin, ListView):
    model = EventTalk
    template_name = u'events/event.html'
    context_object_name = 'talks'

    def dispatch(self, request, *args, **kwargs):
        reponse = super(TalkListView, self).dispatch(request, *args, **kwargs)

        if not self.event.external_link:
            return reponse
        else:
            return redirect(self.event.external_link)

    def get_queryset(self):
        qs = EventTalk.active.filter(event__slug=self.kwargs['event_slug'])
        qs = qs.select_related('talk', 'event')

        return qs.order_by('start', 'talk__type')


class JoinEvent(EventMixin, SimpleTemplateView):
    pass
