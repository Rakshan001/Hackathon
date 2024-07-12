from django.contrib import admin
from .models import Event, Registration

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'event_name', 'date', 'venue', 'event_type', 'seats')
    list_filter = ('date', 'event_type')

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('student', 'event', 'registration_date')
    list_filter = ('event__event_name', 'student__name')

admin.site.register(Event, EventAdmin)
admin.site.register(Registration, RegistrationAdmin)
