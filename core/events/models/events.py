from autoslug import AutoSlugField
from django.db import models
from django_prose_editor.fields import ProseEditorField
from multiselectfield import MultiSelectField
from shortuuid.django_fields import ShortUUIDField

from core.events.models.abstracts import Presentation
from core.profiles.utils.validate_image import clean_image

category = (
    ('Research', 'Research'),
    ('Innovation', 'Innovation'),
    ('Teaching and Learning', 'Teaching and Learning'),
    ('Patents', 'Patents'),
    ('Collaboration', 'Collaboration'),
    ('Grants and Funding', 'Grants and Funding'),
)


class Event(Presentation):
    event_id = ShortUUIDField(
        length=12, max_length=40, alphabet='webcfdr1234', unique=True, editable=False, primary_key=True
    )
    title = models.CharField(max_length=100, help_text='event title')
    slug = AutoSlugField(populate_from='title', unique_with=['event_id', 'date_published'])
    event_description_one = ProseEditorField(max_length=950, null=True, blank=True)
    event_description_two = ProseEditorField(max_length=950, null=True, blank=True)
    tags = models.CharField(max_length=200)
    category = MultiSelectField(
        max_length=100, choices=category, default='Research', null=True, blank=True, help_text='select event category'
    )
    speakers = models.CharField(max_length=700, help_text='event speakers names separated by commas')
    speaker_titles = models.CharField(
        max_length=700, null=True, blank=True, help_text="in order of speaker's name appearance separated by commas"
    )
    speaker_image_1 = models.ImageField(
        upload_to='events/images',
        validators=[clean_image],
        help_text="speaker image 1*. upload in order of speaker's name appearance above"
    )
    speaker_image_2 = models.ImageField(
        upload_to='events/images',
        validators=[clean_image],
        null=True,
        blank=True,
        help_text="speaker image 2. upload in order of speaker's name appearance above"
    )
    speaker_image_3 = models.ImageField(
        upload_to='events/images',
        validators=[clean_image],
        null=True,
        blank=True,
        help_text="speaker image 3. upload in order of speaker's name appearance above"
    )
    speaker_image_4 = models.ImageField(
        upload_to='events/images',
        validators=[clean_image],
        null=True,
        blank=True,
        help_text="speaker image 4. upload in order of speaker's name appearance above"
    )
    speaker_image_5 = models.ImageField(
        upload_to='events/images',
        validators=[clean_image],
        null=True,
        blank=True,
        help_text="speaker image 4. upload in order of speaker's name appearance above"
    )
    speaker_image_6 = models.ImageField(
        upload_to='events/images',
        validators=[clean_image],
        null=True,
        blank=True,
        help_text="speaker image 4. upload in order of speaker's name appearance above"
    )
    speaker_image_7 = models.ImageField(
        upload_to='events/images',
        validators=[clean_image],
        null=True,
        blank=True,
    )
    event_location = models.CharField(max_length=100, help_text='event venue', null=True, blank=True)
    event_lat_long = models.CharField(max_length=100, help_text='event latitude and longitude', null=True, blank=True)
    event_start_time = models.DateTimeField(null=True, blank=True)
    event_end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.title.capitalize()} Details'

    class Meta:
        ordering = ['-date_published']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
