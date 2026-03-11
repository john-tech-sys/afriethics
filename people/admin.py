from django.contrib import admin

from .models import TeamMember, Testimonial, Founder, BoardMember, GovernanceStructure


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("name", "role", "bio")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("author_name", "author_title", "order", "is_published")
    list_editable = ("order", "is_published")
    search_fields = ("author_name", "author_title", "quote")


@admin.register(Founder)
class FounderAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("name", "certification", "bio")
    fieldsets = (
        ("Personal Information", {
            "fields": ("name", "title", "certification", "bio", "photo")
        }),
        ("Contact & Social", {
            "fields": ("email", "linkedin_url", "twitter_url")
        }),
        ("Status", {
            "fields": ("is_active", "order")
        }),
    )


@admin.register(BoardMember)
class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "member_type", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter = ("member_type", "is_active")
    search_fields = ("name", "position", "bio")
    fieldsets = (
        ("Member Information", {
            "fields": ("name", "position", "expertise", "member_type", "bio", "photo")
        }),
        ("Contact & Social", {
            "fields": ("email", "linkedin_url")
        }),
        ("Status", {
            "fields": ("is_active", "order")
        }),
    )


@admin.register(GovernanceStructure)
class GovernanceStructureAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published")
    list_filter = ("is_published",)
    search_fields = ("title", "description")
    fieldsets = (
        ("Governance Information", {
            "fields": ("title", "description")
        }),
        ("Publishing", {
            "fields": ("is_published",)
        }),
    )
