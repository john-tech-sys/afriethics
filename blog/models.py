from __future__ import annotations

from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=Post.Status.PUBLISHED, published_at__lte=timezone.now())


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)

    excerpt = models.TextField(blank=True)
    content = RichTextField('Details', help_text="Main post content. You can paste formatted text/HTML.")

    cover_image = models.ImageField(upload_to="blog/", blank=True)

    status = models.CharField(max_length=12, choices=Status.choices, default=Status.DRAFT)
    published_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PostQuerySet.as_manager()

    class Meta:
        ordering = ["-published_at", "-id"]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("blog:detail", kwargs={"slug": self.slug})

