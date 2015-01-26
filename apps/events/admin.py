# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms

from suit_ckeditor.widgets import CKEditorWidget

from .models import Event, EventTalk, Sponsor, Support


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        widgets = {
            'full_description': CKEditorWidget(
                editor_options={'startupFocus': True}
            )
        }


class EventTalkInline(admin.StackedInline):
    model = EventTalk
    extra = 1


class EventAdmin(admin.ModelAdmin):
    inlines = (EventTalkInline,)
    list_display = ('description', 'date', 'submission_deadline', 'index')
    search_fields = ('description',)
    form = EventForm


admin.site.register(Event, EventAdmin)
admin.site.register(Sponsor)
admin.site.register(Support)
