# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Location, Event, Talk

admin.site.register(Location)
admin.site.register(Event)
admin.site.register(Talk)
