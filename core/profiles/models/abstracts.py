import pgcrypto
from django.db import models
from django.utils import timezone

# level selection
research_type = (
    ('Diploma', 'Diploma'),
    ('Undergraduate', 'Undergraduate'),
    ('Graduate', 'Graduate'),
    ('Masters', 'Masters'),
    ('PHD', 'PHD'),
    ('Post Doctorate', 'Post Doctorate'),
)

# graduate status selection
graduate_choice = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

# research status
research_status = (
    ('Completed', 'Completed'),
    ('Ongoing', 'Ongoing'),
)


class Bio(models.Model):
    research_type = pgcrypto.EncryptedCharField(
        max_length=50, choices=research_type, default='PHD', help_text='ongoing research type'
    )
    research_status = pgcrypto.EncryptedCharField(
        max_length=50, choices=research_status, default='Ongoing', help_text='research status: ongoing or completed'
    )
    graduate_status = pgcrypto.EncryptedCharField(
        max_length=50, choices=graduate_choice, default='No', help_text='researcher has graduated'
    )
    graduation_date = pgcrypto.EncryptedDateField(
        max_length=100, null=True, blank=True, help_text='graduation date if graduation status is completed'
    )
    industry_job = pgcrypto.EncryptedDateField(
        max_length=100, null=True, blank=True, help_text='job in industry if graduation status is completed'
    )
    linkedin_url = pgcrypto.EncryptedCharField(max_length=200, null=True, blank=True, help_text='linkedin link')
    google_scholar_url = pgcrypto.EncryptedCharField(
        max_length=200, null=True, blank=True, help_text='google scholar link'
    )
    researchgate_url = pgcrypto.EncryptedCharField(
        max_length=200, null=True, blank=True, help_text='researchgate link'
    )
    publish = models.BooleanField(default=True, help_text='make profile visible')
    creation_date = models.DateTimeField(auto_now_add=True, help_text='date user account was created')
    timestamp = pgcrypto.EncryptedDateTimeField(default=timezone.now)

    class Meta:
        abstract = True
