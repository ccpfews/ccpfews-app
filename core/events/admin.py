from django import forms
from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.utils.safestring import mark_safe
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm

from .models.events import Event


class EventResource(resources.ModelResource):

    class Meta:
        model = Event
        skip_unchanged = True
        report_skipped = True

    def export(self, queryset=None, *args, **kwargs):
        """
        override the export action by disabling it
        and rendering an error page
        """
        raise PermissionDenied


class EventAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    resource_class = EventResource
    list_display = ['title', 'speakers', 'category', 'tags', 'publish', 'date_updated']
    list_display_links = ['title', 'speakers', 'category', 'date_updated']
    list_filter = ['publish', 'category']
    search_fields = ['title', 'speakers', 'category', 'tags']
    readonly_fields = ['event_id']
    list_per_page = 50
    show_full_result_count = True
    actions_on_top = True
    actions_on_bottom = True
    save_as = True
    save_as_continue = True
    save_on_top = True

    fieldsets = [
        [
            'Book Info',
            {
                'classes': ['wide'],
                'fields': ['event_id', 'title', 'category', 'tags'],
            },
        ],
        [
            'Event Details',
            {
                'classes': ['collapse', 'wide'],
                'fields': ['event_description_one', 'event_description_two'],
            },
        ],
        [
            'Speaker Info',
            {
                'classes': ['collapse', 'wide'],
                'fields': [
                    'speakers', 'speaker_titles', 'speaker_image_1', 'speaker_image_2', 'speaker_image_3',
                    'speaker_image_4', 'speaker_image_5', 'speaker_image_6', 'speaker_image_7'
                ],
            },
        ],
        [
            'More Info',
            {
                'classes': ['collapse', 'wide'],
                'fields': ['event_location', 'event_lat_long', 'event_start_time', 'event_end_time'],
            },
        ],
        [
            'Media Info',
            {
                'classes': ['collapse', 'wide'],
                'fields': [
                    'featured_image', 'gallery_image_1', 'gallery_image_2', 'gallery_image_3', 'gallery_image_4',
                    'gallery_image_5', 'gallery_image_6'
                ],
            },
        ],
        [
            'Publish/Timestamp',
            {
                'classes': ['collapse', 'wide'],
                'fields': ['publish', 'post_scheduling', 'date_published', 'date_updated'],
            },
        ],
    ]

    # override field
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            # redeclare label with a class
            label = mark_safe(
                f'<label class="font-medium mb-2 text-gray-900 text-sm dark:text-gray-200">{db_field.verbose_name}</label>'  # noqa: E501
            )
            # Override the status field to use MultipleChoiceField with SelectMultiple widget
            kwargs['widget'] = forms.SelectMultiple(
                attrs={
                    'class':
                        'border bg-white font-medium min-w-20 rounded-md shadow-sm text-gray-500 text-sm focus:ring focus:ring-primary-300 focus:border-primary-600 focus:outline-none group-[.errors]:border-red-600 group-[.errors]:focus:ring-red-200 dark:bg-gray-900 dark:border-gray-700 dark:text-gray-400 dark:focus:border-primary-600 dark:focus:ring-primary-700 dark:focus:ring-opacity-50 dark:group-[.errors]:border-red-500 dark:group-[.errors]:focus:ring-red-600/40 px-3 py-2 w-full pr-8 max-w-2xl appearance-none',  # noqa: E501
                    'style':
                        'height: 120px;'  # Set the height for the select field
                }
            )
            kwargs['choices'] = [
                ('Research', 'Research'),
                ('Innovation', 'Innovation'),
                ('Teaching and Learning', 'Teaching and Learning'),
                ('Patents', 'Patents'),
                ('Collaboration', 'Collaboration'),
                ('Grants and Funding', 'Grants and Funding'),
            ]
            kwargs['label'] = label
            kwargs['help_text'] = db_field.help_text
            kwargs['initial'] = ['Research']

            return forms.MultipleChoiceField(**kwargs)
        return super().formfield_for_dbfield(db_field, request, **kwargs)


# register model
admin.site.register(Event, EventAdmin)
