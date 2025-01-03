from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

from core.profiles.utils.validate_image import clean_image


class Presentation(models.Model):
    featured_image = models.ImageField(
        upload_to='events/images', validators=[clean_image], help_text='event featured image'
    )
    gallery_image_1 = models.ImageField(
        upload_to='events/images',
        validators=[clean_image],
        null=True,
        blank=True,
        help_text='additional event images'
    )
    gallery_image_2 = models.ImageField(
        upload_to='events/images',
        validators=[clean_image],
        null=True,
        blank=True,
        help_text='additional event images'
    )
    gallery_image_3 = models.ImageField(
        upload_to='events/images',
        validators=[clean_image],
        null=True,
        blank=True,
        help_text='additional event images'
    )
    gallery_image_4 = models.ImageField(
        upload_to='events/images',
        validators=[clean_image],
        null=True,
        blank=True,
        help_text='additional event images'
    )
    gallery_image_5 = models.ImageField(
        upload_to='events/images',
        validators=[clean_image],
        null=True,
        blank=True,
        help_text='additional event images'
    )
    gallery_image_6 = models.ImageField(
        upload_to='events/images',
        validators=[clean_image],
        null=True,
        blank=True,
        help_text='additional event images'
    )
    history = HistoricalRecords(inherit=True)
    publish = models.BooleanField(default=True)
    post_scheduling = models.DateTimeField(
        default=timezone.now,
        verbose_name='Post Scheduling',
        help_text='post now or set date and time to post last later;\
                                                post publish has to be ticked for this to work',
    )
    date_published = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(
        default=timezone.now, verbose_name='Date/Time Updated', help_text='dated last updated'
    )

    class Meta:
        abstract = True
