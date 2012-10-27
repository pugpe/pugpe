from django.contrib import admin

from .models import Signature, Attendee


admin.site.register(Signature)
admin.site.register(Attendee)
