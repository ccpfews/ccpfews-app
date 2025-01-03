from django.contrib import admin
from django.forms import TextInput
from pgcrypto import EncryptedCharField, EncryptedDateTimeField, EncryptedEmailField
from unfold.admin import ModelAdmin

from .models import Consultation, Contact


class ContactMessageAdmin(ModelAdmin):
    list_display = ['full_name', 'email', 'subject', 'has_read', 'date_received']
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
    fields = ['full_name', 'email', 'subject', 'message', 'has_read', 'date_received']

    # override field display
    def formfield_for_dbfield(self, db_field, **kwargs):
        if isinstance(db_field, (EncryptedCharField, EncryptedEmailField, EncryptedDateTimeField)):
            kwargs['widget'] = TextInput(
                attrs={
                    'size':
                        '10',
                    'class':
                        'border bg-white font-medium rounded-md shadow-sm text-gray-500 text-sm focus:ring focus:ring-primary-300 focus:border-primary-600 focus:outline-none group-[.errors]:border-red-600 group-[.errors]:focus:ring-red-200 dark:bg-gray-900 dark:border-gray-700 dark:text-gray-400 dark:focus:border-primary-600 dark:focus:ring-primary-700 dark:focus:ring-opacity-50 dark:group-[.errors]:border-red-500 dark:group-[.errors]:focus:ring-red-600/40 px-3 py-2 w-full max-w-2xl'  # noqa: E501
                }
            )
        return super().formfield_for_dbfield(db_field, **kwargs)


class ConsultationMessageAdmin(ModelAdmin):
    list_display = ['consult_name', 'consult_email', 'has_read', 'date_received']
    list_display_links = ['consult_name', 'consult_email', 'date_received']
    date_hierarchy = 'date_received'
    list_per_page = 50
    actions_on_top = True
    actions_on_bottom = True
    readonly_fields = ['consult_name', 'consult_email', 'consult_message', 'date_received']
    save_as = True
    save_as_continue = True
    save_on_top = True
    search_fields = ['consult_name', 'consult_email', 'date_received']
    fields = ['consult_name', 'consult_email', 'consult_message', 'has_read', 'date_received']

    # override field display
    def formfield_for_dbfield(self, db_field, **kwargs):
        if isinstance(db_field, (EncryptedCharField, EncryptedEmailField, EncryptedDateTimeField)):
            kwargs['widget'] = TextInput(
                attrs={
                    'size':
                        '10',
                    'class':
                        'border bg-white font-medium rounded-md shadow-sm text-gray-500 text-sm focus:ring focus:ring-primary-300 focus:border-primary-600 focus:outline-none group-[.errors]:border-red-600 group-[.errors]:focus:ring-red-200 dark:bg-gray-900 dark:border-gray-700 dark:text-gray-400 dark:focus:border-primary-600 dark:focus:ring-primary-700 dark:focus:ring-opacity-50 dark:group-[.errors]:border-red-500 dark:group-[.errors]:focus:ring-red-600/40 px-3 py-2 w-full max-w-2xl'  # noqa: E501
                }
            )
        return super().formfield_for_dbfield(db_field, **kwargs)


admin.site.register(Contact, ContactMessageAdmin)
admin.site.register(Consultation, ConsultationMessageAdmin)
