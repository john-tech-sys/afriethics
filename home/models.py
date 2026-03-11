from django.urls import reverse

from autoslug import AutoSlugField
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from afriethis import settings
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from engagement.models import Partnership, WhyPartnerWithUs, AreasOfPartnership



class Section(models.Model):
    name = models.CharField(max_length=500)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    call_to_url = models.CharField(max_length=500, default="/")
    image = models.ImageField(upload_to = 'section/', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Section"


class Pages(models.Model):
    name = models.CharField(max_length=500)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to = 'section/', blank=True, null=True)
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING, related_name='section', blank=True, null=True)
    active = models.BooleanField(default=True)
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pages"

@receiver(pre_save, sender=Pages)
def populate_slug(sender, instance, **kwargs):
	instance.slug = slugify(instance.name)


class Home(models.Model):
    policies = models.ForeignKey(Pages, on_delete=models.DO_NOTHING, related_name='policies', blank=True, null=True)
    terms = models.ForeignKey(Pages, on_delete=models.DO_NOTHING, related_name='terms', blank=True, null=True)
    disclaimer = models.ForeignKey(Pages, on_delete=models.DO_NOTHING, related_name='disclaimer', blank=True, null=True)
    home = models.ForeignKey(Pages, on_delete=models.DO_NOTHING, related_name='home', blank=True, null=True)
    about = models.ForeignKey(Pages, on_delete=models.DO_NOTHING, related_name='about', blank=True, null=True)
    apply = models.ForeignKey(Pages, on_delete=models.DO_NOTHING, related_name='apply', blank=True, null=True)
    donate = models.ForeignKey(Pages, on_delete=models.DO_NOTHING, related_name='donate', blank=True, null=True)
    faq = models.ForeignKey(Pages, on_delete=models.DO_NOTHING, related_name='faq', blank=True, null=True)
    carreers = models.ForeignKey(Pages, on_delete=models.DO_NOTHING, related_name='carreers', blank=True, null=True)
    service = models.ForeignKey(Pages, on_delete=models.DO_NOTHING, related_name='service', blank=True, null=True)

    def __str__(self):
        return "Home"

    class Meta:
        verbose_name = "Home"


class HomepageHeroSlide(models.Model):
    headline = models.CharField(max_length=140)
    subheadline = models.TextField(blank=True)
    image = models.ImageField(upload_to="hero/", blank=True)
    cta_label = models.CharField(max_length=60, blank=True)
    cta_url = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self) -> str:
        return self.headline


class Page(models.Model):
    """Editable content pages (used for About, Problem/Why we exist, etc.)."""

    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    summary = models.TextField(blank=True)
    body = models.TextField(blank=True, help_text="You can paste simple HTML from the old site.")

    show_in_nav = models.BooleanField(default=False)
    nav_label = models.CharField(max_length=60, blank=True)
    nav_order = models.PositiveIntegerField(default=0)

    is_published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nav_order", "title"]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("core:page", kwargs={"slug": self.slug})



class Ethos(models.Model):
    vision = models.TextField(blank=True, null=True)
    mission = models.TextField(blank=True, null=True)
    call_to_url = models.CharField(max_length=500, default="/")
    image = models.ImageField(upload_to = 'section/', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.vision

    class Meta:
        verbose_name_plural = "Ethos"


class Values(models.Model):
    title = models.CharField(blank=True, null=True)
    label = models.CharField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    call_to_url = models.CharField(max_length=500, default="/")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Values"


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.name


class AboutPage(models.Model):
    """Editable About Us page sections"""
    section_type = models.CharField(
        max_length=50,
        choices=[
            ('background', 'Background & Story'),
            ('mission_vision', 'Mission, Vision & Values'),
            ('founders', 'Our Founders'),
            ('governance', 'Governance & Leadership'),
            ('transparency', 'Transparency'),
        ]
    )
    
    title = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(upload_to='about/', blank=True)
    
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        unique_together = ["section_type"]

    def __str__(self) -> str:
        return f"{self.get_section_type_display()}"


class AnnualReport(models.Model):
    """Annual reports and financial statements for transparency"""
    year = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    pdf_file = models.FileField(upload_to='reports/')
    summary = models.TextField(blank=True)
    
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-year"]

    def __str__(self) -> str:
        return f"{self.title} ({self.year})"


    class Meta:
        verbose_name_plural = "Countries"


class Discipline(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class HappyCustomers(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='customers/', blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Process(models.Model):
    title = models.CharField(max_length=100)
    number = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class HomeTestimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    message = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
