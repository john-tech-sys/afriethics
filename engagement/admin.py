from django.contrib import admin

from .models import ContactMessage, PartnerProposal, VolunteerApplication, Resource, DonationOption


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "contact_date")
    search_fields = ("name", "email", "message")
    date_hierarchy = "contact_date"


@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "area_of_interest", "created_at")
    search_fields = ("full_name", "email", "phone_number", "area_of_interest", "motivation")
    date_hierarchy = "created_at"


@admin.register(PartnerProposal)
class PartnerProposalAdmin(admin.ModelAdmin):
    list_display = ("organization_name", "email", "collaboration_type", "created_at")
    search_fields = ("organization_name", "contact_person", "email", "phone_number", "message")
    date_hierarchy = "created_at"


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "resource_type", "is_published")
    list_filter = ("resource_type", "is_published")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("published_at", "updated_at")
    fieldsets = (
        ("Resource Information", {
            "fields": ("title", "slug", "resource_type", "description", "thumbnail")
        }),
        ("Content", {
            "fields": ("file", "external_url"),
            "description": "Either upload a file or provide an external URL"
        }),
        ("Publishing", {
            "fields": ("is_published", "published_at", "updated_at")
        }),
    )


@admin.register(DonationOption)
class DonationOptionAdmin(admin.ModelAdmin):
    list_display = ("title", "amount", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title", "description", "impact")
    fieldsets = (
        ("Donation Tier", {
            "fields": ("title", "amount", "icon")
        }),
        ("Details", {
            "fields": ("description", "impact")
        }),
        ("Status", {
            "fields": ("is_active", "order")
        }),
    )
