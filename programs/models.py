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





