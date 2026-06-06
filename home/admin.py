from django.contrib import admin

from .models import (
    Section, Pages, Country, Home, HomepageHeroSlide, Page, Ethos, Values,
    AboutPage, AnnualReport, HappyCustomers, Feedback, HomeTestimonial,
    IntroVideo, ProblemPage,
    Partnership, WhyPartnerWithUs, AreasOfPartnership
)


class ProcessAdmin(admin.ModelAdmin):
    list_display = ['title', 'number']
    list_per_page = 10


class DisciplineAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    list_per_page = 10


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'active')
    search_fields = ('name', 'title')


@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'section', 'active')
    list_filter = ('active', 'section')
    search_fields = ('name', 'title')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(HomepageHeroSlide)
class HomepageHeroSlideAdmin(admin.ModelAdmin):
    list_display = ('headline', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('headline',)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'show_in_nav', 'nav_order', 'is_published', 'updated_at')
    list_editable = ('show_in_nav', 'nav_order', 'is_published')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'summary', 'body')


@admin.register(Ethos)
class EthosAdmin(admin.ModelAdmin):
    list_display = ('vision', 'active')
    search_fields = ('vision', 'mission')


@admin.register(Values)
class ValuesAdmin(admin.ModelAdmin):
    list_display = ('title', 'label', 'order', 'active')
    list_editable = ('order', 'active')
    search_fields = ('title', 'label', 'description')


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('get_section_type_display', 'title', 'order', 'is_published')
    list_editable = ('order', 'is_published')
    list_filter = ('section_type', 'is_published')
    search_fields = ('title', 'content')
    readonly_fields = ('updated_at',)
    fieldsets = (
        ('Page Information', {
            'fields': ('section_type', 'title', 'image')
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('Publishing', {
            'fields': ('order', 'is_published', 'updated_at')
        }),
    )


@admin.register(AnnualReport)
class AnnualReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'is_published', 'updated_at')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'year')
    search_fields = ('title', 'description')
    readonly_fields = ('published_at', 'updated_at')
    fieldsets = (
        ('Report Information', {
            'fields': ('year', 'title', 'description')
        }),
        ('Document', {
            'fields': ('pdf_file', 'summary')
        }),
        ('Publishing', {
            'fields': ('is_published', 'published_at', 'updated_at')
        }),
    )


@admin.register(HappyCustomers)
class HappyCustomersAdmin(admin.ModelAdmin):
    pass


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass


@admin.register(IntroVideo)
class IntroVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle', 'thumbnail')
        }),
        ('Video Source', {
            'description': 'Provide either an embed URL (YouTube/Vimeo) or upload an MP4 file.',
            'fields': ('embed_url', 'video_file')
        }),
        ('Publishing', {
            'fields': ('is_active',)
        }),
    )


@admin.register(HomeTestimonial)
class HomeTestimonialAdmin(admin.ModelAdmin):
    pass


@admin.register(Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    pass


@admin.register(WhyPartnerWithUs)
class WhyPartnerWithUsAdmin(admin.ModelAdmin):
    pass


@admin.register(AreasOfPartnership)
class AreasOfPartnershipAdmin(admin.ModelAdmin):
    pass


@admin.register(ProblemPage)
class ProblemPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'badge_text', 'is_published', 'updated_at')
    list_editable = ('is_published',)
    readonly_fields = ('updated_at',)
    fieldsets = (
        ('Hero Section', {
            'fields': ('badge_text', 'section_title', 'intro_description')
        }),
        ('Challenge Block', {
            'fields': ('challenge_title', 'challenge_body')
        }),
        ('Source Attribution', {
            'fields': ('source_label', 'source_url')
        }),
        ('Closing Statement', {
            'fields': ('closing_statement',)
        }),
        ('Call to Action', {
            'fields': (
                'cta_header',
                ('cta_volunteer_text', 'cta_volunteer_url'),
                ('cta_partner_text', 'cta_partner_url'),
                ('cta_programs_text', 'cta_programs_url'),
            )
        }),
        ('Publishing', {
            'fields': ('is_published', 'updated_at')
        }),
    )
