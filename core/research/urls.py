from django.urls import path

from .views import ProjectDetails, ProjectView, ResearchView  # type: ignore

urlpatterns = [
    path('project/<slug:slug>/details/', ProjectDetails.as_view(), name='project_details'),
    path('projects/', ProjectView.as_view(), name='project_listings'),
    path('', ResearchView.as_view(), name='research'),
]
