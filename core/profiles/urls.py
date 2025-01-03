from django.urls import path

from .views import Team, TeamDetails  # type: ignore

urlpatterns = [
    path('', Team.as_view(), name='team_listings'),
    path('<slug:slug>/details/', TeamDetails.as_view(), name='team_details'),
]
