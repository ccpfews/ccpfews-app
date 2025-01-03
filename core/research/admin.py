from django import forms
from django.contrib import admin, messages
from django.core.exceptions import PermissionDenied
from django.utils.safestring import mark_safe
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm

from .models.books import Book
from .models.journals import Journal
from .models.projects import Project


@admin.display(description='Publish/Unpublish Selection')
def publish_action(modeladmin, request, querryset):
    if querryset.filter(publish=True):
        querryset.update(publish=False)
        messages.add_message(request, messages.SUCCESS, 'selected list unpublished successfully')
    else:
        querryset.update(publish=True)
        messages.add_message(request, messages.SUCCESS, 'selected list published successfully')


class ProjectResource(resources.ModelResource):

    class Meta:
        model = Project
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ['project_id']

    def export(self, queryset=None, *args, **kwargs):
        """
        override the export action by disabling it
        and rendering an error page
        """
        raise PermissionDenied


class BookAdmin(ModelAdmin):
    list_display = ['title', 'author', 'category', 'tags', 'publish', 'date_updated']
    list_display_links = ['title', 'author', 'category', 'date_updated']
    list_filter = ['publish', 'category']
    search_fields = ['title', 'author', 'category', 'tags']
    readonly_fields = ['post_id']
    list_per_page = 50
    show_full_result_count = True
    actions = [publish_action]
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
                'fields': ['post_id', 'title', 'category', 'tags', 'author', 'publish_url'],
            },
        ],
        [
            'Abstract Info',
            {
                'classes': ['collapse', 'wide'],
                'fields': ['abstract'],
            },
        ],
        [
            'Media Info',
            {
                'classes': ['collapse', 'wide'],
                'fields': [
                    'featured_image', 'gallery_image_1', 'gallery_image_2', 'gallery_image_3', 'gallery_image_4'
                ],
            },
        ],
        [
            'Publish/Timestamp',
            {
                'classes': ['collapse', 'wide'],
                'fields': ['publish', 'schedule_publish', 'date_updated'],
            },
        ],
    ]


class JournalAdmin(ModelAdmin):
    list_display = ['title', 'author', 'category', 'tags', 'publish', 'date_updated']
    list_display_links = ['title', 'author', 'category', 'date_updated']
    list_filter = ['publish', 'category']
    search_fields = ['title', 'author', 'category', 'tags']
    readonly_fields = ['post_id']
    list_per_page = 50
    show_full_result_count = True
    actions = [publish_action]
    actions_on_top = True
    actions_on_bottom = True
    save_as = True
    save_as_continue = True
    save_on_top = True

    fieldsets = [
        [
            'Journal Info',
            {
                'classes': ['wide'],
                'fields': ['post_id', 'author', 'title', 'category', 'tags', 'google_scholar_url', 'researchgate_url'],
            },
        ],
        [
            'Abstract Info',
            {
                'classes': ['collapse', 'wide'],
                'fields': ['abstract'],
            },
        ],
        [
            'Media Info',
            {
                'classes': ['collapse', 'wide'],
                'fields': [
                    'featured_image', 'gallery_image_1', 'gallery_image_2', 'gallery_image_3', 'gallery_image_4'
                ],
            },
        ],
        [
            'Publish/Timestamp',
            {
                'classes': ['collapse', 'wide'],
                'fields': ['publish', 'schedule_publish', 'date_updated'],
            },
        ],
    ]


class ProjectAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    resource_class = ProjectResource
    list_display = ['title', 'category', 'tags', 'status', 'publish', 'date_updated']
    list_display_links = ['title', 'category', 'date_updated']
    list_filter = ['publish', 'category', 'status']
    search_fields = ['title', 'other_innovators', 'category', 'tags']
    readonly_fields = ['project_id']
    list_per_page = 50
    show_full_result_count = True
    actions = [publish_action]
    actions_on_top = True
    actions_on_bottom = True
    save_as = True
    save_as_continue = True
    save_on_top = True

    fieldsets = [
        [
            'Project Info',
            {
                'classes': ['wide'],
                'fields': ['project_id', 'title', 'author', 'category', 'tags', 'status'],
            },
        ],
        [
            'Project Details',
            {
                'classes': ['collapse', 'wide'],
                'fields': ['project_description_one', 'project_description_two'],
            },
        ],
        [
            'Other Project Innovators',
            {
                'classes': ['collapse', 'wide'],
                'fields': [
                    'other_innovators', 'other_innovator_image_1', 'other_innovator_image_2',
                    'other_innovator_image_3', 'other_innovator_image_4'
                ],
            },
        ],
        [
            'Gallery',
            {
                'classes': ['collapse', 'wide'],
                'fields': [
                    'image', 'gallery_image_1', 'gallery_image_2', 'gallery_image_3', 'gallery_image_4',
                    'gallery_image_5', 'gallery_image_6'
                ],
            },
        ],
        [
            'Publish/Timestamp',
            {
                'classes': ['collapse', 'wide'],
                'fields': ['publish', 'post_scheduling', 'date_updated'],
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
admin.site.register(Book, BookAdmin)
admin.site.register(Journal, JournalAdmin)
admin.site.register(Project, ProjectAdmin)
