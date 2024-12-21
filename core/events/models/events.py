from autoslug import AutoSlugField
from django.db import models
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
    event_id = ShortUUIDField(length=38, max_length=40, alphabet='webcfdr1234', primary_key=True)
    title = models.CharField(max_length=100, help_text='event title')
    slug = AutoSlugField(populate_from='title', unique_with=['event_id', 'date_published'])
    about = models.TextField(max_length=5000, help_text='event descriptions')
    tags = models.CharField(max_length=200)
    speakers = models.CharField(max_length=100, help_text='event speakers')
    category = MultiSelectField(
        max_length=100, choices=category, default='Research', help_text='select event category'
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

    def __str__(self):
        return f'{self.title.capitalize()} Details'

    class Meta:
        ordering = ['-date_published']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
