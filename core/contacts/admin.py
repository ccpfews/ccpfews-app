from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.forms import Textarea, TextInput  # noqa: I101
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from pgcrypto import EncryptedCharField, EncryptedDateTimeField, EncryptedEmailField, EncryptedTextField
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm

from .models import Consultation, Contact


class ImportExportResource(resources.ModelResource):

    class Meta:
        model = Contact
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ['id']

    def export(self, queryset=None, *args, **kwargs):
        """
        override the export action by disabling it
        and rendering an error page
        """
        raise PermissionDenied


class ContactMessageAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    resource_class = ImportExportResource
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


class ConsultationMessageAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    resource_class = ImportExportResource
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
        elif isinstance(db_field, (EncryptedTextField)):
            kwargs['widget'] = Textarea(
                attrs={
                    'cols':
                        40,
                    'rows':
                        '10',
                    'class':
                        'vLargeTextField border bg-white font-medium min-w-20 rounded-md shadow-sm text-font-default-light text-sm focus:ring focus:ring-primary-300 focus:border-primary-600 focus:outline-none group-[.errors]:border-red-600 group-[.errors]:focus:ring-red-200 dark:bg-gray-900 dark:border-gray-700 dark:text-font-default-dark dark:focus:border-primary-600 dark:focus:ring-primary-700 dark:focus:ring-opacity-50 dark:group-[.errors]:border-red-500 dark:group-[.errors]:focus:ring-red-600/40 px-3 py-2 w-full max-w-4xl appearance-none expandable transition transition-height duration-75 ease-in-out'  # noqa: E501
                }
            )
        return super().formfield_for_dbfield(db_field, **kwargs)


admin.site.register(Contact, ContactMessageAdmin)
admin.site.register(Consultation, ConsultationMessageAdmin)
