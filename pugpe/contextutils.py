from django.conf import settings


def facebook(context):
    return {'FACEBOOK_APP_ID': settings.FACEBOOK_APP_ID}


def now(context):
    from django.utils import timezone
    return{
        'date_now': timezone.now(),
    }
