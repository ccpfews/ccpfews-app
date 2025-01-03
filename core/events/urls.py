from django.urls import path

from .views import EventDetails, EventPost

urlpatterns = [
    path('', EventPost.as_view(), name='event_listings'),
    path('<slug:slug>/details/', EventDetails.as_view(), name='event_details'),
]
