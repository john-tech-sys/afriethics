from django.contrib import admin

from .models import Program, SuccessStory


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_published", "updated_at")
    list_editable = ("order", "is_published")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "summary", "description")



@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "published_at")
    list_filter = ("is_published", "published_at")
    search_fields = ("title", "summary", "description")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("updated_at", "published_at")
    fieldsets = (
        ("Story Information", {
            "fields": ("title", "slug", "featured_image")
        }),
        ("Content", {
            "fields": ("summary", "description", "impact_highlight")
        }),
        ("Relationship", {
            "fields": ("related_program",)
        }),
        ("Publishing", {
            "fields": ("is_published", "published_at", "updated_at")
        }),
    )
