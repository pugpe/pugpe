# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^emails/', include('emails.urls', namespace='emails')),
    url(r'^cert/', include('cert.urls', namespace='cert')),
    url(r'^archive/', include('archive.urls', namespace='archive')),

    url(r'^xx/$', direct_to_template, {'template': 'events/xx.html'}),
    url(r'^sobre/$', direct_to_template, {'template': 'about.html'}, name='about'),

    url(r'^', include('events.urls', namespace='events')),
    url(r'^(?P<event_slug>[\w_-]+)/submissao/',
        include('submission.urls', namespace='submission'),
    ),
    url(r'_health/$', 'core.views.health', name='health'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
