# -*- coding:utf-8 -*-
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

from events.models import Event
from events.views import EventMixin

from .models import Talk
from .forms import TalkForm, VoteForm
from .utils import token_required


class SubmissionView(EventMixin, CreateView):
    form_class = TalkForm
    template_name = 'submission/submission.html'
    model = Talk

    def get_success_url(self):
        return reverse('submission:success_submission', kwargs=self.kwargs)

    def get_form_kwargs(self):
        kwargs = super(SubmissionView, self).get_form_kwargs()
        kwargs['event'] = Event.objects.get(slug=self.kwargs['event_slug'])

        return kwargs


class SubmissionListView(EventMixin, ListView):
    model = Talk
    template_name = 'submission/vote.html'
    context_object_name = 'talks'
    paginate_by = 1

    @method_decorator(token_required)
    def dispatch(self, *args, **kwargs):
        return super(SubmissionListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Talk.objects.filter(type__in=['talk', 'tutorial'])

    def post(self, request, *args, **kwargs):
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save(request.session['email'])

        page = request.POST.get('page', None)
        if page is None:
            return redirect(reverse('submission:success', kwargs=self.kwargs))

        return redirect(
            reverse('submission:vote', kwargs=self.kwargs) +
            '?page={0}'.format(page),
        )
