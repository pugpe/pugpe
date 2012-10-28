from django.contrib import admin

from .models import Signature, Attendee


class AttendeeAdmin(admin.ModelAdmin):
    model = Attendee
    exclude = ('sent_date', 'slug')
    save_as = True
    search_fields = ('email', 'name')


admin.site.register(Signature)
admin.site.register(Attendee, AttendeeAdmin)
