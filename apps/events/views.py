# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse

from .models import Event, EventTalk, EventParticipants
from .models import Support, Sponsor

from django.views.generic import RedirectView


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


class JoinEvent(EventMixin, RedirectView):

    def dispatch(self, request, *args, **kwargs):
        kwargs['user'] = request.user
        return super(JoinEvent, self).dispatch(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        user = kwargs['user']
        if user:
            if not self.event in user.event_set.all():
                participant = EventParticipants(user=user, event=self.event)
                participant.save()

        return reverse('events:event', kwargs={'event_slug': self.event.slug})
