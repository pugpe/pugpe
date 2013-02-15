# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Talk

class TalkAdmin(admin.ModelAdmin):

    list_display = ('title', 'name', 'email', 'type', 'macro_theme', 'level')
    list_filter = ('type', 'macro_theme', 'level')
    search_fields = ('title', 'name', 'email')

admin.site.register(Talk, TalkAdmin)