from django.conf.urls import patterns, include, url

from .views import TalkListView, JoinEvent


urlpatterns = patterns('',
    url(r'^(?P<event_slug>[\w_-]+)/$',
        TalkListView.as_view(),
        name='event',
    ),

    url(r'^(?P<event_slug>[\w_-]+)/participar/$',
        JoinEvent.as_view(),
        name='participate',
    ),
)
