from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from .views import SubmissionView, SubmissionListView


urlpatterns = patterns('',
    url(r'^$',
        SubmissionView.as_view(),
        name='submission',
    ),
    url(r'^success/$',
        direct_to_template, {'template': 'submission/success_submission.html'},
        name='success_submission',
    ),

    url(r'^votar/$',
        SubmissionListView.as_view(),
        name='vote',
    ),
    url(r'^votar/erro/$',
        direct_to_template, {'template': 'submission/error.html'},
        name='error',
    ),
    url(r'^votar/success/$',
        direct_to_template, {'template': 'submission/success.html'},
        name='success',
    ),
)
