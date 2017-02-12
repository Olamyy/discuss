from django.contrib import admin
from .models import Attendee, Sponsor, Contact
from event import email


def send_email(modeladmin, request, queryset):
    print("Yes")


send_email.short_description = "Send email"


class AttendeeAdmin(admin.ModelAdmin):
    actions = [send_email]


admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Sponsor)
admin.site.register(Contact)
