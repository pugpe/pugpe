from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from events.models import Event


def index(request):
    ev = Event.objects.filter(index=True).order_by('-id')
    if ev.exists():
        return redirect(
            reverse('events:event', kwargs={'event_slug': ev[0].slug}),
        )
    else:
        return render(request, 'index.html', {})


class SimpleTemplateView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(SimpleTemplateView, self).get_context_data(**kwargs)

        context.update(context['param'])
        return context
