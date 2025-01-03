import pgcrypto
from django.db import models
from django.utils import timezone


class Contact(models.Model):
    full_name = pgcrypto.EncryptedCharField(max_length=100)
    email = pgcrypto.EncryptedEmailField(max_length=254)
    phone = pgcrypto.EncryptedCharField(max_length=254, default='12345')
    subject = pgcrypto.EncryptedCharField(max_length=100)
    message = pgcrypto.EncryptedTextField(max_length=5000)
    has_read = models.BooleanField(default=False, help_text='admin has read message')
    date_received = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['date_received']


class Consultation(models.Model):
    consult_name = pgcrypto.EncryptedCharField(max_length=100, help_text='fullname')
    consult_email = pgcrypto.EncryptedEmailField(max_length=254)
    consult_message = pgcrypto.EncryptedTextField(max_length=5000)
    has_read = models.BooleanField(default=False, help_text='admin has read message')
    date_received = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.consult_name

    class Meta:
        verbose_name = 'Consultation'
        verbose_name_plural = 'Consultations'
        ordering = ['date_received']
