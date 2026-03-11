from __future__ import annotations

from .models import NavigationLink, SiteConfiguration


def site_context(request):
    settings = SiteConfiguration.objects.first()
    nav_links = NavigationLink.objects.filter(is_active=True).order_by("order", "label")
    return {"site_settings": settings, "nav_links": nav_links}
