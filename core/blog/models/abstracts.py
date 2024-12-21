from autoslug import AutoSlugField
from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField

from core.profiles.models.profiles import Profile
from core.profiles.utils.validate_image import clean_image

category = (
    ('Research', 'Research'),
    ('Innovation', 'Innovation'),
    ('Webinar', 'Webinar'),
    ('Showcase', 'Showcase'),
    ('Funding', 'Funding'),
    ('News/Events', 'News/Events'),
)


class Post(models.Model):
    title = models.CharField(max_length=100, help_text='enter post title')
    slug = AutoSlugField(populate_from='title', unique_with=[
        'date_published',
    ])
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = MultiSelectField(choices=category, default='Research', max_length=100)
    post = models.TextField(max_length=5000)
    tags = models.CharField(max_length=500)
    featured_image = models.ImageField(upload_to='blog/images', validators=[clean_image])
    publish = models.BooleanField(default=True)
    date_published = models.DateTimeField(auto_now_add=True)
    schedule_publish = models.DateTimeField(
        default=timezone.now,
        help_text='Schedule when this post should become visible on the site. \
                            <span style="color:red;">Note: Publish must be ticked for this to work</span>'
    )
    date_updated = models.DateTimeField(default=timezone.now, verbose_name='Date/Time', help_text='dated last updated')

    class Meta:
        abstract = True
