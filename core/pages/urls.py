from django.urls import path

from .views import About, Home  # type: ignore

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
]
