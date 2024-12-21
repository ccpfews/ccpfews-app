from django.contrib import admin
from unfold.admin import ModelAdmin

from .models.events import Event


class EventAdmin(ModelAdmin):
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
                'fields': ['about'],
            },
        ],
        [
            'Speaker Info',
            {
                'classes': ['collapse', 'wide'],
                'fields': ['speakers', 'speaker_image_1', 'speaker_image_2', 'speaker_image_3', 'speaker_image_4'],
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


# register model
admin.site.register(Event, EventAdmin)
