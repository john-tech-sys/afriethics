from __future__ import annotations

from django.views.generic import ListView

from .models import TeamMember, Testimonial


class TeamListView(ListView):
    template_name = "people/team.html"
    context_object_name = "team"

    def get_queryset(self):
        return TeamMember.objects.filter(is_active=True).order_by("order", "name")


class TestimonialListView(ListView):
    template_name = "people/testimonials.html"
    context_object_name = "testimonials"

    def get_queryset(self):
        return Testimonial.objects.filter(is_published=True).order_by("order", "id")
