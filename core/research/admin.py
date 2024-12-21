from django.contrib import admin, messages
from unfold.admin import ModelAdmin

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


class ProjectAdmin(ModelAdmin):
    list_display = ['title', 'innovators', 'category', 'tags', 'status', 'publish', 'date_updated']
    list_display_links = ['title', 'innovators', 'category', 'date_updated']
    list_filter = ['publish', 'category', 'status']
    search_fields = ['title', 'innovators', 'category', 'tags']
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
                'fields': ['project_id', 'innovators', 'title', 'category', 'tags', 'status'],
            },
        ],
        [
            'Project Details',
            {
                'classes': ['collapse', 'wide'],
                'fields': ['about'],
            },
        ],
        [
            'Media Info',
            {
                'classes': ['collapse', 'wide'],
                'fields': ['image', 'gallery_image_1', 'gallery_image_2', 'gallery_image_3', 'gallery_image_4'],
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


# register model
admin.site.register(Book, BookAdmin)
admin.site.register(Journal, JournalAdmin)
admin.site.register(Project, ProjectAdmin)
