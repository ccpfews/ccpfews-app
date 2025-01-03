from defender.models import AccessAttempt
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.sites.models import Site
from django.forms import Textarea, TextInput  # noqa: I101
from django.utils.safestring import mark_safe
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from pgcrypto import (
    EncryptedCharField, EncryptedDateField, EncryptedDateTimeField, EncryptedEmailField, EncryptedTextField
)
from simple_history import register
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm

from .models.profiles import Profile
from .utils.admin.register_defender import AttemptAdmin
from .utils.admin.register_groups import UserGroupAdmin
from .utils.admin.register_sites import UserSiteAdmin


class ProfileResource(resources.ModelResource):

    class Meta:
        model = Profile
        skip_unchanged = True
        report_skipped = True
        import_id_fields = [
            'research_type', 'research_status', 'graduate_status', 'graduation_date', 'industry_job', 'linkedin_url',
            'google_scholar_url', 'researchgate_url', 'publish', 'title', 'first_name', 'last_name', 'role', 'email',
            'gender', 'about', 'short_bio', 'qualifications', 'skillset'
        ]
        exclude = ['profile_id', 'image']
        export_id_fields = ['profile_id']


class ProfileAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    resource_class = ProfileResource
    list_display = [
        'mask_profile_id', 'title', 'role', 'first_name', 'last_name', 'gender', 'research_type', 'research_status',
        'graduate_status', 'publish'
    ]
    list_display_links = ['title', 'role', 'first_name', 'last_name', 'gender', 'research_type', 'research_status']
    list_filter = ['gender', 'research_type', 'research_status', 'graduate_status', 'publish']
    search_fields = ['first_name', 'last_name']
    readonly_fields = ['mask_profile_id']
    date_hierarchy = 'creation_date'
    list_per_page = 20
    show_full_result_count = True
    actions_on_top = True
    actions_on_bottom = True
    save_as = True
    save_as_continue = True
    save_on_top = True

    fieldsets = [
        [
            'General Information',
            {
                'classes': ['wide', 'extrapretty'],
                'fields': ['mask_profile_id', 'first_name', 'last_name', 'email', 'gender', 'title', 'role'],
            },
        ],
        [
            'Bio Details',
            {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': [
                    'about', 'short_bio', 'qualifications', 'qualification_schools', 'qualification_years', 'skillset'
                ],
            },
        ],
        [
            'Research Details',
            {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': ['research_type', 'research_status'],
            },
        ],
        [
            'Graduate Details',
            {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': ['graduate_status', 'graduation_date', 'industry_job'],
            },
        ],
        [
            'Links', {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': ['linkedin_url', 'google_scholar_url', 'researchgate_url']
            }
        ],
        [
            'Profile Image',
            {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': ['image'],
            },
        ],
        [
            'Publish Details',
            {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': ['publish', 'timestamp'],
            },
        ],
    ]

    # override field display
    def formfield_for_dbfield(self, db_field, request=None, **kwargs):

        choice_fields = ['research_type', 'graduate_status', 'research_status', 'gender']
        encrypted_fields = (EncryptedCharField, EncryptedEmailField, EncryptedDateTimeField, EncryptedDateField)

        if db_field.name not in choice_fields and isinstance(db_field, encrypted_fields):
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
        elif db_field.name in choice_fields:
            # label
            label = mark_safe(
                f'<label class="font-medium mb-2 text-gray-900 text-sm dark:text-gray-200">'
                f'{db_field.verbose_name}</label>'
            )

            # choice selection
            selected_choice = []

            if db_field.name == 'research_type':
                selected_choice = [
                    ('Diploma', 'Diploma'),
                    ('Undergraduate', 'Undergraduate'),
                    ('Graduate', 'Graduate'),
                    ('Masters', 'Masters'),
                    ('PHD', 'PHD'),
                    ('Post Doctorate', 'Post Doctorate'),
                ]
            elif db_field.name == 'graduate_status':
                selected_choice = [
                    ('Yes', 'Yes'),
                    ('No', 'No'),
                ]
            elif db_field.name == 'research_status':
                selected_choice = [
                    ('Completed', 'Completed'),
                    ('Ongoing', 'Ongoing'),
                ]
            elif db_field.name == 'gender':
                selected_choice = [
                    ('Male', 'Male'),
                    ('Female', 'Female'),
                ]
            # create selection
            field = forms.ChoiceField(
                choices=selected_choice,
                label=label,
                initial='Masters',  # default selected option
                help_text=db_field.help_text,
            )

            # widget
            field.widget.attrs.update({
                'class': (
                    'border bg-white font-medium min-w-20 rounded-md shadow-sm '
                    'text-gray-500 text-sm focus:ring focus:ring-primary-300 '
                    'focus:border-primary-600 focus:outline-none group-[.errors]:border-red-600 '
                    'group-[.errors]:focus:ring-red-200 dark:bg-gray-900 dark:border-gray-700 '
                    'dark:text-gray-400 dark:focus:border-primary-600 dark:focus:ring-primary-700 '
                    'dark:focus:ring-opacity-50 dark:group-[.errors]:border-red-500 '
                    'dark:group-[.errors]:focus:ring-red-600/40 px-3 py-2 w-full pr-8 max-w-2xl appearance-none'
                ),
                'style': 'height: 40px;',
            })

            return field

        return super().formfield_for_dbfield(db_field, request, **kwargs)

    # show profile image
    @admin.display(description='image')
    def profile_image(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width=obj.image.width,
                height=obj.image.height,
            )
        )

    # add custom field for email
    @admin.display(description='email')
    def mask_email(self, obj):
        return '**********.uj.ac.za'

    # add custom field for registration id
    @admin.display(description='profile id')
    def mask_profile_id(self, obj):
        return '********'


# register admin settings
admin.site.register(Profile, ProfileAdmin)

# register axes in unfold template
admin.site.register(AccessAttempt, AttemptAdmin)
# register groups in unfold template
admin.site.register(Group, UserGroupAdmin)
# register sites in unfold template
admin.site.register(Site, UserSiteAdmin)
# simple history model registry
register(Group)
register(User)
register(Site)
