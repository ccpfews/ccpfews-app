from django.urls import path

from .views import ConsultView, ContactPage

urlpatterns = [
    path('', ContactPage.as_view(), name='contact'),
    path('consultation/', ConsultView.as_view(), name='consult'),
]
