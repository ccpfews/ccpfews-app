from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from shortuuid.django_fields import ShortUUIDField

from core.research.models.abstracts import Publication, clean_image


class Journal(Publication):
    post_id = ShortUUIDField(length=38, max_length=40, alphabet='abctfs6r1234', primary_key=True)
    slug = AutoSlugField(
        populate_from='title',
        unique_with=['post_id', 'date_published'],
    )
    gallery_image_1 = models.ImageField(
        upload_to='blog/images', validators=[clean_image], help_text='additional journal images'
    )
    gallery_image_2 = models.ImageField(
        upload_to='blog/images', validators=[clean_image], help_text='additional journal images'
    )
    gallery_image_3 = models.ImageField(
        upload_to='blog/images', validators=[clean_image], help_text='additional journal images'
    )
    gallery_image_4 = models.ImageField(
        upload_to='blog/images', validators=[clean_image], help_text='additional journal images'
    )
    google_scholar_url = models.URLField(null=True, blank=True, help_text='journal google scholar link')
    researchgate_url = models.URLField(null=True, blank=True, help_text='journal researchgate link')

    def __str__(self):
        return f'{self.title.capitalize()} Details'

    class Meta:
        ordering = ['-date_published']
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'

    def get_absolute_url(self):
        return reverse('journal_details', kwargs={'slug': self.slug})
