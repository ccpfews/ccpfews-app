import pgcrypto
from django.db import models
from django.utils import timezone


class Contact(models.Model):
    full_name = pgcrypto.EncryptedCharField(max_length=100)
    email = pgcrypto.EncryptedEmailField(max_length=254)
    subject = pgcrypto.EncryptedCharField(max_length=100)
    message = pgcrypto.EncryptedTextField(max_length=5000)
    date_received = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_subject

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['date_received']
