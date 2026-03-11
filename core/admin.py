from django.contrib import admin

from .models import NavigationLink, SiteSettings, FocusArea, ImpactMetric


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "address")


@admin.register(NavigationLink)
class NavigationLinkAdmin(admin.ModelAdmin):
    list_display = ("label", "url", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("label", "url")


@admin.register(FocusArea)
class FocusAreaAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "icon")
    list_editable = ("order",)
    search_fields = ("name", "description")


@admin.register(ImpactMetric)
class ImpactMetricAdmin(admin.ModelAdmin):
    list_display = ("name", "value", "order", "icon")
    list_editable = ("order",)
    search_fields = ("name", "description")
