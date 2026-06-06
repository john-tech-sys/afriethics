from __future__ import annotations

from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Program(models.Model):
    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    summary = models.TextField(blank=True)
    description = RichTextField(blank=True)

    image = models.ImageField(upload_to="programs/", blank=True)

    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("programs:detail", kwargs={"slug": self.slug})


class SuccessStory(models.Model):
    """Case studies and success stories from programs"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    description = RichTextField()
    
    featured_image = models.ImageField(upload_to="success_stories/", blank=True)
    
    related_program = models.ForeignKey(Program, on_delete=models.SET_NULL, blank=True, null=True, related_name="success_stories")
    
    impact_highlight = models.CharField(max_length=200, blank=True, help_text="e.g., '500 lives changed'")
    
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("programs:story-detail", kwargs={"slug": self.slug})


class ProfessionalServiceCategory(models.Model):
    """Categories for Professional Services"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField(blank=True)
    description = RichTextField(blank=True)
    icon = models.CharField(max_length=100, blank=True, help_text="Font Awesome icon class, e.g., 'fas fa-shield-alt'")
    image = models.ImageField(upload_to="professional_services/categories/", blank=True)
    
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "title"]
        verbose_name_plural = "Professional Service Categories"

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("programs:professional-services-category", kwargs={"slug": self.slug})


class ProfessionalService(models.Model):
    """Individual professional services within categories"""
    category = models.ForeignKey(ProfessionalServiceCategory, on_delete=models.CASCADE, related_name="services")
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    description = RichTextField()
    
    featured_image = models.ImageField(upload_to="professional_services/", blank=True)
    
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "title"]
        verbose_name_plural = "Professional Services"

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("programs:professional-services-detail", kwargs={"slug": self.slug})


