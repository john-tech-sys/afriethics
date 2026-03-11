from __future__ import annotations

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Program, Event, SuccessStory


class ProgramListView(ListView):
    template_name = "programs/program_list.html"
    context_object_name = "programs"

    def get_queryset(self):
        return Program.objects.filter(is_published=True).order_by("order", "title")


class ProgramDetailView(DetailView):
    template_name = "programs/program_detail.html"
    context_object_name = "program"

    def get_object(self, queryset=None):
        return get_object_or_404(Program, slug=self.kwargs["slug"], is_published=True)


class EventListView(ListView):
    template_name = "programs/event_list.html"
    context_object_name = "events"
    paginate_by = 12

    def get_queryset(self):
        return Event.objects.filter(is_published=True).order_by("-event_date")


class EventDetailView(DetailView):
    model = Event
    template_name = "programs/event_detail.html"
    context_object_name = "event"

    def get_object(self, queryset=None):
        return get_object_or_404(Event, slug=self.kwargs["slug"], is_published=True)


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

