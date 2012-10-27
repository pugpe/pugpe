from django.conf.urls import patterns, include, url


urlpatterns = patterns('cert.views',
    url(r'^(?P<token>.*)/$',
        'certificate',
        name='certificate',
    ),
)
