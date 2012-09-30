# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Location, Event, Talk, EventTalk


class EventTalkInline(admin.StackedInline):
    model = EventTalk
    extra = 1


class EventAdmin(admin.ModelAdmin):
    inlines = (EventTalkInline,)

admin.site.register(Location)
admin.site.register(Event, EventAdmin)
admin.site.register(Talk)
