from __future__ import annotations

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView

from core.models import FocusArea, ImpactMetric
from people.models import Testimonial

from .models import Program, SuccessStory



class ProgramsImpactView(TemplateView):
    template_name = "core/programs_impact.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["programs"] = Program.objects.filter(is_published=True).order_by("order", "title")
        ctx["success_stories"] = SuccessStory.objects.filter(is_published=True).order_by("-published_at")
        ctx["testimonials"] = Testimonial.objects.filter(is_published=True).order_by("order", "id")
        ctx["impact_metrics"] = ImpactMetric.objects.filter(is_active=True).order_by("order", "name")
        ctx["focus_areas"] = FocusArea.objects.filter(is_active=True).order_by("order", "name")
        return ctx



class ProgramDetailView(DetailView):
    template_name = "programs/program_detail.html"
    context_object_name = "program"

    def get_object(self, queryset=None):
        return get_object_or_404(Program, slug=self.kwargs["slug"], is_published=True)


class SuccessStoryListView(ListView):
    template_name = "programs/story_list.html"
    context_object_name = "stories"
    paginate_by = 9

    def get_queryset(self):
        return SuccessStory.objects.filter(is_published=True).order_by("-published_at")


class SuccessStoryDetailView(DetailView):
    model = SuccessStory
    template_name = "programs/story_detail.html"
    context_object_name = "story"

    def get_object(self, queryset=None):
        return get_object_or_404(SuccessStory, slug=self.kwargs["slug"], is_published=True)

