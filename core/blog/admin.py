from django.contrib import admin, messages
from django.utils.html import format_html
from django.utils.timezone import datetime, utc
from unfold.admin import ModelAdmin

from .models.blogs import Blog


@admin.display(description='Publish/Unpublish Selection')
def publish_action(modeladmin, request, querryset):
    if querryset.filter(publish=True):
        querryset.update(publish=False)
        messages.add_message(request, messages.SUCCESS, 'selected list unpublished successfully')
    else:
        querryset.update(publish=True)
        messages.add_message(request, messages.SUCCESS, 'selected list published successfully')


class BlogAdmin(ModelAdmin):
    list_display = ['title', 'author', 'category', 'publish', 'schedule_post', 'date_updated']
    list_display_links = ['title', 'author', 'category', 'date_updated']
    list_editable = ['publish']
    list_filter = ['publish']
    search_fields = ['title', 'author', 'category', 'post', 'tags', 'publish', 'date_updated']
    date_hierarchy = 'date_updated'
    list_per_page = 50
    show_full_result_count = True
    actions = [publish_action]
    actions_on_top = True
    actions_on_bottom = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    view_on_site = True
    fieldsets = [
        ['Info', {
            'classes': ['wide', 'extrapretty'],
            'fields': ['title', 'author', 'category', 'tags']
        }],
        ['Details', {
            'classes': ['collapse', 'wide', 'extrapretty'],
            'fields': ['post']
        }],
        [
            'Media', {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': [
                    'featured_image', 'gallery_image_1', 'gallery_image_2', 'gallery_image_3', 'gallery_image_4'
                ]
            }
        ],
        [
            'Visibility', {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': ['publish', 'schedule_publish', 'date_updated']
            }
        ],
    ]

    @admin.display(description='Post Schedule')
    def schedule_post(self, obj):
        if obj.schedule_publish > datetime.now().replace(tzinfo=utc):
            return format_html(
                '<span style="color:white; background:#DD3438; font-size:14px; padding: 5px 8px; border:1px solid red; border-radius:10px;">*Yes</span>'  # noqa: E501
            )
        else:
            return format_html(
                '<span style="color:#453F3F; font-weight:bolder; background:#CBCBCB; font-size:14px; padding: 5px 8px; border:1px solid #453F3F; border-radius:10px;">*No</span>'  # noqa: E501
            )


admin.site.register(Blog, BlogAdmin)
