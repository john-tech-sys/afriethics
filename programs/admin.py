from django.contrib import admin

from .models import Program, SuccessStory, ProfessionalServiceCategory, ProfessionalService


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


@admin.register(ProfessionalServiceCategory)
class ProfessionalServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_published", "updated_at")
    list_editable = ("order", "is_published")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "summary", "description")
    fieldsets = (
        ("Category Information", {
            "fields": ("title", "slug", "icon", "image")
        }),
        ("Content", {
            "fields": ("summary", "description")
        }),
        ("Publishing", {
            "fields": ("order", "is_published", "updated_at")
        }),
    )


@admin.register(ProfessionalService)
class ProfessionalServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "order", "is_published", "updated_at")
    list_editable = ("order", "is_published")
    list_filter = ("category", "is_published")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "summary", "description")
    readonly_fields = ("updated_at", "created_at")
    fieldsets = (
        ("Service Information", {
            "fields": ("title", "slug", "category", "featured_image")
        }),
        ("Content", {
            "fields": ("summary", "description")
        }),
        ("Publishing", {
            "fields": ("order", "is_published", "created_at", "updated_at")
        }),
    )
