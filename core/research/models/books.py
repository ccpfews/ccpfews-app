from autoslug import AutoSlugField
from django.db import models
from shortuuid.django_fields import ShortUUIDField

from core.research.models.abstracts import Publication, clean_image


class Book(Publication):
    post_id = ShortUUIDField(length=38, max_length=40, alphabet='abcgfdr1234', primary_key=True)
    slug = AutoSlugField(
        populate_from='title',
        unique_with=['post_id', 'date_published'],
    )
    gallery_image_1 = models.ImageField(
        upload_to='blog/images', validators=[clean_image], help_text='additional book images'
    )
    gallery_image_2 = models.ImageField(
        upload_to='blog/images', validators=[clean_image], help_text='additional book images'
    )
    gallery_image_3 = models.ImageField(
        upload_to='blog/images', validators=[clean_image], help_text='additional book images'
    )
    gallery_image_4 = models.ImageField(
        upload_to='blog/images', validators=[clean_image], help_text='additional book images'
    )
    publish_url = models.URLField(null=True, blank=True, help_text='book url link')

    def __str__(self):
        return f'{self.title.capitalize()} Details'

    class Meta:
        ordering = ['-date_published']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
