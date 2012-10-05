# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'index.html'}, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^emails/', include('emails.urls', namespace='emails')),
    url(r'^', include('events.urls', namespace='events')),
    url(r'^(?P<event_slug>[\w_-]+)/submissao/',
        include('submission.urls', namespace='submission')
    ),
)
