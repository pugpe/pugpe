from django.conf.urls import patterns, include, url

from .views import PastEvents


urlpatterns = patterns('',
    url(r'^past_events/$',
        PastEvents.as_view(),
        name='past_events'
    ),
)
