import pgcrypto
from autoslug import AutoSlugField
from django.db import models
from shortuuid.django_fields import ShortUUIDField
from simple_history.models import HistoricalRecords

from core.profiles.models.abstracts import Bio
from core.profiles.utils.validate_image import clean_image

# gender selection
gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class Profile(Bio):
    profile_id = ShortUUIDField(length=38, max_length=40, alphabet='abcdefg1234', primary_key=True)
    slug = AutoSlugField(populate_from='first_name', unique_with=['profile_id'], default='', editable=True)
    title = pgcrypto.EncryptedCharField(max_length=100, null=True, blank=True)
    first_name = pgcrypto.EncryptedCharField(max_length=100, null=True, blank=True)
    last_name = pgcrypto.EncryptedCharField(max_length=100, null=True, blank=True)
    role = pgcrypto.EncryptedCharField(max_length=100, null=True, blank=True, help_text='role held in the center')
    email = pgcrypto.EncryptedEmailField(unique=True)
    gender = pgcrypto.EncryptedCharField(max_length=50, choices=gender, default='Female')
    about = pgcrypto.EncryptedTextField(max_length=2000, null=True, blank=True, verbose_name='Bio')
    short_bio = pgcrypto.EncryptedTextField(max_length=400, null=True, blank=True, help_text='abridged bio details')
    qualifications = pgcrypto.EncryptedTextField(
        max_length=2000, null=True, blank=True, help_text='list separated with commas'
    )
    qualification_schools = pgcrypto.EncryptedTextField(
        max_length=2000,
        null=True,
        blank=True,
        help_text='school of graduation in order of qualification listings separated with commas'
    )
    qualification_years = pgcrypto.EncryptedTextField(
        max_length=2000,
        null=True,
        blank=True,
        help_text='year of graduation in order of qualification listings separated with commas'
    )
    skillset = pgcrypto.EncryptedTextField(max_length=2000)
    image = models.ImageField(
        upload_to='profiles', validators=[clean_image], null=True, blank=True, help_text='profile image'
    )
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['-creation_date']
        permissions = (('import', 'Can import'),)
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
