from autoslug import AutoSlugField
from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
from shortuuid.django_fields import ShortUUIDField

from core.research.models.abstracts import category, clean_image, status


class Project(models.Model):
    project_id = ShortUUIDField(length=38, max_length=40, alphabet='axa6r1234', primary_key=True)
    title = models.CharField(max_length=100, help_text='project title')
    slug = AutoSlugField(populate_from='title', unique_with=['date_published'])
    about = models.TextField(max_length=5000)
    tags = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=status, default='Completed', help_text='select project status')
    innovators = models.CharField(max_length=100, help_text='project innovators')
    category = MultiSelectField(
        max_length=100, choices=category, default='Research', help_text='select project category'
    )
    image = models.ImageField(
        upload_to='projects/images', validators=[clean_image], help_text='project featured image'
    )
    gallery_image_1 = models.ImageField(
        upload_to='projects/images', validators=[clean_image], help_text='additional project images'
    )
    gallery_image_2 = models.ImageField(
        upload_to='projects/images', validators=[clean_image], help_text='additional project images'
    )
    gallery_image_3 = models.ImageField(
        upload_to='projects/images', validators=[clean_image], help_text='additional project images'
    )
    gallery_image_4 = models.ImageField(
        upload_to='projects/images', validators=[clean_image], help_text='additional project images'
    )
    publish = models.BooleanField(default=True)
    post_scheduling = models.DateTimeField(
        default=timezone.now,
        verbose_name='Post Scheduling',
        help_text='post now or set date and time to post last later;\
                                                post publish has to be ticked for this to work',
    )
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(default=timezone.now, verbose_name='Date/Time', help_text='dated last updated')

    def __str__(self):
        return f'{self.title.capitalize()} Details'

    class Meta:
        ordering = ['-date_published']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
