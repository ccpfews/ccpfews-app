from django.contrib import admin
from django.forms import TextInput
from django.utils.safestring import mark_safe
from import_export import resources
from import_export.admin import ImportMixin
from pgcrypto import EncryptedCharField, EncryptedDateTimeField, EncryptedEmailField
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm

from .models.profiles import Profile


class ProfileResource(resources.ModelResource):

    class Meta:
        model = Profile
        skip_unchanged = True
        report_skipped = True
        import_id_fields = [
            'first_name', 'last_name', 'email', 'gender', 'research_type', 'research_status', 'graduate_status',
            'graduation_date', 'industry_job', 'bio', 'short_bio', 'qualification', 'skillset', 'linkedin_url',
            'google_scholar_url', 'researchgate_url'
        ]
        exclude = ['profile_id', 'image', 'data_import_finish']
        export_id_fields = ['profile_id']

    def before_import_row(self, row, row_number=None, **kwargs):
        get_title = row['title']
        get_role = row['role']
        get_first_name = row['first_name']
        get_last_name = row['last_name'],
        get_email = row['email'],
        get_gender = row['gender'],
        get_research_type = row['research_type'],
        get_research_status = row['research_status']
        get_graduate_status = row['user_status'],
        get_graduation_date = row['graduation_date'],
        get_industry_job = row['industry_job'],
        get_bio = row['bio'],
        get_short_bio = row['short_bio']
        get_qualification = row['qualification'],
        get_skillset = row['skillset'],
        get_linkedin_url = row['linkedin_url'],
        get_google_scholar_url = row['google_scholar_url'],
        get_researchgate_url = row['researchgate_url'],
        try:
            # check if object exist
            existing_obj = self._meta.model.objects.filter(email__in=[get_email])

            if existing_obj:
                # check if the records has changed
                existing_obj_unchanged = self._meta.model.objects.filter(
                    title__in=get_title,
                    role__in=get_role,
                    first_name__in=get_first_name,
                    last_name__in=get_last_name,
                    email__in=get_email,
                    gender__in=get_gender,
                    research_type__in=get_research_type,
                    research_status__in=get_research_status,
                    graduate_status__in=get_graduate_status,
                    graduation_date__in=get_graduation_date,
                    industry_job__in=get_industry_job,
                    bio__in=get_bio,
                    short_bio__in=get_short_bio,
                    qualification__in=get_qualification,
                    skillset__in=get_skillset,
                    linkedin_url__in=get_linkedin_url,
                    google_scholar_url__in=get_google_scholar_url,
                    researchgate_url__in=get_researchgate_url,
                ).exists()

                if existing_obj_unchanged is False:
                    # Attempt to get the existing object
                    get_existing_obj = self._meta.model.objects.get(email__in=[get_email])

                    get_existing_obj.tile = get_title[0],
                    get_existing_obj.role = get_role[0],
                    get_existing_obj.first_name = get_first_name[0],
                    get_existing_obj.last_name = get_last_name[0],
                    get_existing_obj.email = get_email[0],
                    get_existing_obj.gender = get_gender[0],
                    get_existing_obj.research_type = get_research_type[0],
                    get_existing_obj.research_status = get_research_status[0]
                    get_existing_obj.graduate_status = get_graduate_status[0],
                    get_existing_obj.graduation_date = get_graduation_date[0],
                    get_existing_obj.industry_job = get_industry_job[0],
                    get_existing_obj.bio = get_bio[0],
                    get_existing_obj.short_bio = get_short_bio[0],
                    get_existing_obj.qualification = get_qualification[0],
                    get_existing_obj.skillset = get_skillset[0],
                    get_existing_obj.linkedin_url = get_linkedin_url[0],
                    get_existing_obj.google_scholar_url = get_google_scholar_url[0],
                    get_existing_obj.researchgate_url = get_researchgate_url[0],

                    # save record
                    get_existing_obj.save(
                        update_fields=[
                            'title', 'role', 'first_name', 'last_name', 'email', 'gender', 'research_type',
                            'research_status', 'graduate_status', 'graduation_date', 'industry_job', 'bio',
                            'short_bio', 'qualification', 'skillset', 'linkedin_url', 'google_scholar_url',
                            'researchgate_url'
                        ]
                    )

                    # updated record
                    get_existing_obj.refresh_from_db()

                    # mark import as an update
                    row['skip_row'] = True
                else:
                    # skip row
                    row['skip_row'] = True

            else:
                # record does not exist
                row['skip_row'] = False

        except self._meta.model.DoesNotExist:
            # Object does not exist, proceed with the import (creation)
            row['skip_row'] = False

    def skip_row(self, instance, original, row, import_validation_errors=None):
        # Skip the row if it is marked as skipped
        return row.get('skip_row', False)


class ProfileAdmin(ImportMixin, ModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    resource_class = ProfileResource
    list_display = [
        'data_import_finish', 'mask_profile_id', 'title', 'role', 'first_name', 'last_name', 'gender', 'research_type',
        'research_status', 'graduate_status'
    ]
    list_display_links = ['mask_profile_id', 'first_name', 'last_name']
    list_filter = ['gender', 'research_type', 'research_status', 'graduate_status', 'publish']
    search_fields = ['first_name', 'last_name']
    readonly_fields = ['data_import_finish', 'mask_profile_id']
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
                'fields': [
                    'data_import_finish', 'mask_profile_id', 'first_name', 'last_name', 'mask_email', 'gender',
                    'title', 'role'
                ],
            },
        ],
        [
            'Bio Details',
            {
                'classes': ['collapse', 'wide', 'extrapretty'],
                'fields': ['bio', 'short_bio', 'qualification', 'skillset'],
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
