from django.conf.urls import patterns, include, url


urlpatterns = patterns('emails.views',
    url(r'^optout/$',
        'optout',
        name='optout',
    ),
)
