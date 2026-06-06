from django.urls import path

from .views import (
    ProgramDetailView, 
    ProgramsImpactView,
    SuccessStoryListView,
    SuccessStoryDetailView,
    ProfessionalServicesListView,
    ProfessionalServiceCategoryDetailView,
    ProfessionalServiceDetailView,
)

app_name = "programs"

urlpatterns = [
    path("", ProgramsImpactView.as_view(), name="list"),
    path("<slug:slug>/", ProgramDetailView.as_view(), name="detail"),
    
    path("stories/", SuccessStoryListView.as_view(), name="story-list"),
    path("stories/<slug:slug>/", SuccessStoryDetailView.as_view(), name="story-detail"),
    
    # Professional Services URLs
    path("professional-services/", ProfessionalServicesListView.as_view(), name="professional-services-list"),
    path("professional-services/category/<slug:slug>/", ProfessionalServiceCategoryDetailView.as_view(), name="professional-services-category"),
    path("professional-services/<slug:slug>/", ProfessionalServiceDetailView.as_view(), name="professional-services-detail"),
]

