from django.urls import path

from .views import (
    ProgramDetailView, 
    ProgramListView,
    EventListView,
    EventDetailView,
    SuccessStoryListView,
    SuccessStoryDetailView,
)

app_name = "programs"

urlpatterns = [
    path("", ProgramListView.as_view(), name="list"),
    path("<slug:slug>/", ProgramDetailView.as_view(), name="detail"),
    
    # Events
    path("events/", EventListView.as_view(), name="event-list"),
    path("events/<slug:slug>/", EventDetailView.as_view(), name="event-detail"),
    
    # Success Stories
    path("stories/", SuccessStoryListView.as_view(), name="story-list"),
    path("stories/<slug:slug>/", SuccessStoryDetailView.as_view(), name="story-detail"),
]

