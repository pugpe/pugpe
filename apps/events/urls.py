from django.conf.urls import patterns, include, url

from .views import TalkListView


urlpatterns = patterns('',
    url(r'^(?P<event_slug>[\w_-]+)$', TalkListView.as_view(), name='event'),
)
