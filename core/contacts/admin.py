from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Contact


class ContactMessageAdmin(ModelAdmin):
    list_display = ['full_name', 'email', 'subject', 'date_received']
    list_display_links = ['full_name', 'email', 'subject', 'date_received']
    date_hierarchy = 'date_received'
    list_per_page = 50
    actions_on_top = True
    actions_on_bottom = True
    readonly_fields = ['full_name', 'email', 'subject', 'message', 'date_received']
    save_as = True
    save_as_continue = True
    save_on_top = True
    search_fields = ['full_name', 'email', 'subject', 'date_received']
    fields = ['full_name', 'email', 'subject', 'message', 'date_received']


admin.site.register(Contact, ContactMessageAdmin)
