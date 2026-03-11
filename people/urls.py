from django.urls import path

from .views import TeamListView, TestimonialListView

app_name = "people"

urlpatterns = [
    path("team/", TeamListView.as_view(), name="team"),
    path("testimonials/", TestimonialListView.as_view(), name="testimonials"),
]
