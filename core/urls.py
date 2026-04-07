from django.urls import path

from django.contrib.sitemaps.views import sitemap
from .views import (
    HomeView, 
    PageDetailView,
    AboutView,
    NewsResourcesView,
    ProgramsImpactView,
    # Legacy views
    AboutMissionVisionView,
    AboutFoundersView,
    AboutGovernanceView,
    AboutTransparencyView,
    ImpactView,
    ResourcesView,
    health,
)
from core import views

sitemaps = {
    'static': views.StaticViewSitemap,
}
app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),    
    path('health', health, name='health'),
    # Consolidated pages
    path("about/", AboutView.as_view(), name="about"),
    path("news-resources/", NewsResourcesView.as_view(), name="news-resources"),
    path("programs-impact/", ProgramsImpactView.as_view(), name="programs-impact"),
    
    # Legacy About Pages (redirect or deprecated)
    path("about/mission-vision/", AboutMissionVisionView.as_view(), name="about-mission"),
    path("about/founders/", AboutFoundersView.as_view(), name="about-founders"),
    path("about/governance/", AboutGovernanceView.as_view(), name="about-governance"),
    path("about/transparency/", AboutTransparencyView.as_view(), name="about-transparency"),
    
    # Legacy Impact & Resources (redirect or deprecated)
    path("impact/", ImpactView.as_view(), name="impact"),
    path("resources/", ResourcesView.as_view(), name="resources"),
    
    # Generic pages
    path("pages/<slug:slug>/", PageDetailView.as_view(), name="page"),
]

