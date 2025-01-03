from bleach import clean  # type: ignore
from django import forms
from django.conf import settings
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

from core.contacts.models import Consultation, Contact  # type: ignore


# custom charfield with bleach to sanitize input
class BleachMarkdownField(forms.CharField):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self, value):
        # configuration for allowed tags and attributes using bleach
        tags = settings.BLEACH_ALLOWED_TAGS
        attributes = settings.BLEACH_ALLOWED_ATTRIBUTES
        cleaned_value = super().clean(value)
        return clean(cleaned_value, tags=tags, attributes=attributes)


class UserContactForm(forms.ModelForm):
    full_name = BleachMarkdownField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
    phone = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    subject = BleachMarkdownField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = BleachMarkdownField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Your Message'}))
    captcha = ReCaptchaField(widget=ReCaptchaV3())

    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone', 'subject', 'message']


class UserConsultationForm(forms.ModelForm):
    consult_name = BleachMarkdownField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    consult_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    consult_message = BleachMarkdownField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Message'}))

    # captcha = ReCaptchaField(widget=ReCaptchaV3())

    class Meta:
        model = Consultation
        fields = ['consult_name', 'consult_email', 'consult_message']
