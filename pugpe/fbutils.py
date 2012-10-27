from django.conf import settings


def app_id(context):
    return {'FACEBOOK_APP_ID': settings.FACEBOOK_APP_ID}
