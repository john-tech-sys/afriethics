from __future__ import annotations

from django.db import models
from ckeditor.fields import RichTextField


class TeamMember(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="team/", blank=True)

    email = models.EmailField(blank=True)
    linkedin_url = models.URLField(blank=True)
    x_url = models.URLField(blank=True)

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self) -> str:
        return self.name


class Founder(models.Model):
    """Organization founders with their background"""
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=160)
    certification = models.CharField(max_length=160, blank=True, help_text="e.g., Certified Fraud Examiner")
    bio = RichTextField(blank=True)
    photo = models.ImageField(upload_to="founders/", blank=True)

    email = models.EmailField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self) -> str:
        return self.name


class BoardMember(models.Model):
    """Board of directors and advisory team members"""
    name = models.CharField(max_length=120)
    position = models.CharField(max_length=160)
    expertise = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="board/", blank=True)

    email = models.EmailField(blank=True)
    linkedin_url = models.URLField(blank=True)

    member_type = models.CharField(
        max_length=50,
        choices=[
            ('director', 'Board Director'),
            ('advisor', 'Advisory Team'),
        ],
        default='director'
    )

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["member_type", "order", "name"]

    def __str__(self) -> str:
        return f"{self.name} ({self.position})"


class GovernanceStructure(models.Model):
    """Governance and organizational structure information"""
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Governance Structure"

    def __str__(self) -> str:
        return self.title


class Testimonial(models.Model):
    quote = models.TextField()
    author_name = models.CharField(max_length=120)
    author_title = models.CharField(max_length=160, blank=True)
    author_photo = models.ImageField(upload_to="testimonials/", blank=True)

    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self) -> str:
        return f"{self.author_name}"  # noqa: D401

