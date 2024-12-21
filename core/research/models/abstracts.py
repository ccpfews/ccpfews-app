from django.db import models
from django.utils import timezone

from core.profiles.models.profiles import Profile
from core.profiles.utils.validate_image import clean_image

status = (
    ('Completed', 'Completed'),
    ('On-going', 'On-going'),
)

category = (
    ('Research', 'Research'),
    ('Innovation', 'Innovation'),
    ('Teaching and Learning', 'Teaching and Learning'),
    ('Patents', 'Patents'),
    ('Collaboration', 'Collaboration'),
    ('Grants and Funding', 'Grants and Funding'),
)


class Publication(models.Model):
    title = models.CharField(max_length=100, help_text='enter post title')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.CharField(max_length=200, help_text='journal categories')
    abstract = models.TextField(max_length=5000)
    tags = models.CharField(max_length=500)
    featured_image = models.ImageField(upload_to='blog/images', validators=[clean_image])
    publish = models.BooleanField(default=True)
    date_published = models.DateTimeField(auto_now_add=True)
    schedule_publish = models.DateTimeField(
        default=timezone.now,
        help_text='Schedule when this post should become visible on the site. \
                            <span style="color:red;">Note: Publish must be ticked for this to work</span>',
    )
    date_updated = models.DateTimeField(default=timezone.now, verbose_name='Date/Time', help_text='dated last updated')

    class Meta:
        abstract = True
