from __future__ import annotations

from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView

from blog.models import Post
from people.models import Testimonial, Founder, BoardMember
from programs.models import Program, SuccessStory
from engagement.models import Resource
from home.models import HomepageHeroSlide, Page, AboutPage, AnnualReport
from core.models import FocusArea, ImpactMetric
from django.http import HttpResponse
from django.contrib.sitemaps import Sitemap



class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'about', 'contact']  # your URL names

    def location(self, item):
        return reverse(item)
    

def health(request):
    return HttpResponse("OK")


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["hero_slides"] = HomepageHeroSlide.objects.filter(is_active=True).order_by("order", "id")
        ctx["programs"] = Program.objects.filter(is_published=True).order_by("order", "title")[:6]
        ctx["latest_posts"] = Post.objects.published().order_by("-published_at")[:3]
        ctx["testimonials"] = Testimonial.objects.filter(is_published=True).order_by("order", "id")[:6]
        ctx["focus_areas"] = FocusArea.objects.filter(is_active=True).order_by("order", "name")
        ctx["impact_metrics"] = ImpactMetric.objects.filter(is_active=True).order_by("order", "name")
        return ctx


class AboutView(TemplateView):
    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["founders"] = Founder.objects.filter(is_active=True).order_by("order", "name")
        ctx["directors"] = BoardMember.objects.filter(member_type='director', is_active=True).order_by("order", "name")
        ctx["advisors"] = BoardMember.objects.filter(member_type='advisor', is_active=True).order_by("order", "name")
        ctx["annual_reports"] = AnnualReport.objects.filter(is_published=True).order_by("-year")
        return ctx


class NewsResourcesView(TemplateView):
    template_name = "core/news_resources.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["posts"] = Post.objects.published().order_by("-published_at")
        ctx["resources"] = Resource.objects.filter(is_published=True).order_by("-published_at")
        return ctx


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


# Legacy views - kept for backward compatibility but could be deprecated
class AboutMissionVisionView(TemplateView):
    template_name = "core/about_mission_vision.html"


class AboutFoundersView(ListView):
    model = Founder
    template_name = "core/about_founders.html"
    context_object_name = "founders"
    queryset = Founder.objects.filter(is_active=True).order_by("order", "name")


class AboutGovernanceView(TemplateView):
    template_name = "core/about_governance.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["directors"] = BoardMember.objects.filter(member_type='director', is_active=True).order_by("order", "name")
        ctx["advisors"] = BoardMember.objects.filter(member_type='advisor', is_active=True).order_by("order", "name")
        return ctx


class AboutTransparencyView(ListView):
    model = AnnualReport
    template_name = "core/about_transparency.html"
    context_object_name = "annual_reports"
    queryset = AnnualReport.objects.filter(is_published=True).order_by("-year")


class ImpactView(TemplateView):
    template_name = "core/impact.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["success_stories"] = SuccessStory.objects.filter(is_published=True).order_by("-published_at")[:6]
        ctx["testimonials"] = Testimonial.objects.filter(is_published=True).order_by("order", "id")[:6]
        return ctx


class ResourcesView(ListView):
    model = Resource
    template_name = "core/resources.html"
    context_object_name = "resources"
    queryset = Resource.objects.filter(is_published=True).order_by("-published_at")


class PageDetailView(DetailView):
    model = Page
    template_name = "core/page.html"
    context_object_name = "page"

    def get_object(self, queryset=None):
        return get_object_or_404(Page, slug=self.kwargs["slug"], is_published=True)

