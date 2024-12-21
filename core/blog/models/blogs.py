from django.db import models
from django.urls import reverse

from core.blog.models.abstracts import Post
from core.profiles.utils.validate_image import clean_image


class Blog(Post):
    gallery_image_1 = models.ImageField(
        upload_to='blog/images', validators=[clean_image], help_text='additional blog images'
    )
    gallery_image_2 = models.ImageField(
        upload_to='blog/images', validators=[clean_image], help_text='additional blog images'
    )
    gallery_image_3 = models.ImageField(
        upload_to='blog/images', validators=[clean_image], help_text='additional blog images'
    )
    gallery_image_4 = models.ImageField(
        upload_to='blog/images', validators=[clean_image], help_text='additional blog images'
    )

    def __str__(self):
        return f'{self.title.capitalize()} Details'

    class Meta:
        ordering = ['-date_published']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def get_absolute_url(self):
        return reverse('blog_details', kwargs={'slug': self.slug})
