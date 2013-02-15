# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Event, EventTalk, Sponsor, Support

class EventTalkInline(admin.StackedInline):
    model = EventTalk
    extra = 1

class EventAdmin(admin.ModelAdmin):
    inlines = (EventTalkInline,)
    list_display = ('description', 'date', 'submission_deadline', 'index')
    search_fields = ('description',)

admin.site.register(Event, EventAdmin)
admin.site.register(Sponsor)
admin.site.register(Support)