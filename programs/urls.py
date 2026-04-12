from django.urls import path

from .views import (
    ProgramDetailView, 
    ProgramsImpactView,
    SuccessStoryListView,
    SuccessStoryDetailView,
)

app_name = "programs"

urlpatterns = [
    path("", ProgramsImpactView.as_view(), name="list"),
    path("<slug:slug>/", ProgramDetailView.as_view(), name="detail"),
    
    path("stories/", SuccessStoryListView.as_view(), name="story-list"),
    path("stories/<slug:slug>/", SuccessStoryDetailView.as_view(), name="story-detail"),
]

