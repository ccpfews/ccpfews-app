from autoslug import AutoSlugField
from django.db import models
from django.utils import timezone
from django_prose_editor.fields import ProseEditorField
from multiselectfield import MultiSelectField
from shortuuid.django_fields import ShortUUIDField
from simple_history.models import HistoricalRecords

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
    post_id = ShortUUIDField(length=12, max_length=15, alphabet='aghrsdfg1234', editable=False, primary_key=True)
    title = models.CharField(max_length=65, help_text='enter post title')
    slug = AutoSlugField(populate_from='title', unique_with=[
        'post_id',
    ])
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = MultiSelectField(choices=category, default='Research', max_length=100)
    post_one = ProseEditorField(max_length=1700)
    post_two = ProseEditorField(max_length=960, null=True, blank=True)
    post_three = ProseEditorField(max_length=960, null=True, blank=True)
    tags = models.CharField(max_length=500)
    featured_image = models.ImageField(upload_to='blog/images', validators=[clean_image])
    publish = models.BooleanField(default=True)
    date_published = models.DateTimeField(default=timezone.now)
    schedule_publish = models.DateTimeField(
        default=timezone.now,
        help_text='Schedule when this post should become visible on the site. \
                            <span style="color:red;">Note: Publish must be ticked for this to work</span>'
    )
    history = HistoricalRecords(inherit=True)
    date_updated = models.DateTimeField(
        default=timezone.now, verbose_name='Update Date/Time', help_text='dated last updated'
    )

    class Meta:
        abstract = True
