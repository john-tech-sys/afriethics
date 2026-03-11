from __future__ import annotations
from datetime import datetime
from ckeditor.fields import RichTextField
from django.db import models


class Contact(models.Model):
    item = models.CharField(max_length=200, blank=True, null=True)
    item_id = models.IntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now)
    user_id = models.IntegerField(blank=True)
    def __str__ (self):
        return self.name

class VolunteerApplication(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50, blank=True)
    area_of_interest = models.CharField(max_length=120, blank=True)
    motivation = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at", "-id"]

    def __str__(self) -> str:
        return self.full_name


class Partnership(models.Model):
    description = RichTextField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=100)
    picture = models.ImageField(upload_to='home/partnership', default='default/partnership.png', null=True)
    content = RichTextField(blank=True, null=True)
    def __str__(self):
        return self.name


class WhyPartnerWithUs(models.Model):
    description = models.TextField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=100)
    field = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.name


class AreasOfPartnership(models.Model):
    description = models.TextField(blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=100)
    picture = models.ImageField(upload_to='home/partnership', default='default/logo.png', null=True)
    field = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.name


class PartnerProposal(models.Model):
    organization_name = models.CharField(max_length=160)
    contact_person = models.CharField(max_length=120, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50, blank=True)
    collaboration_type = models.CharField(max_length=120, blank=True)
    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at", "-id"]

    def __str__(self) -> str:
        return self.organization_name


class Partner(models.Model):
	name = models.CharField(max_length=500, blank=True, null=True)
	url = models.URLField()
	image = models.ImageField(upload_to = 'partners/', default=None, null=True)
	active = models.BooleanField(default=True)

    
class Adress(models.Model):
    country = models.CharField(max_length=200, blank=True, null=True)
    State = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    Adress1 = models.CharField(max_length=200, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    post = models.CharField(max_length=200, blank=True, null=True)
    other = models.TextField(blank=True, null=True)
    def __str__ (self):
        return self.city
    
    class Meta:
        verbose_name_plural='Adress'


# Aliases for backwards compatibility
ContactMessage = Contact


class Resource(models.Model):
    """Research reports, ethics toolkits, guides, training materials, policy briefs"""
    RESOURCE_TYPE_CHOICES = [
        ('research', 'Research Report'),
        ('toolkit', 'Toolkit'),
        ('guide', 'Guide'),
        ('training', 'Training Material'),
        ('brief', 'Policy Brief'),
        ('report', 'Annual Report'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    resource_type = models.CharField(max_length=50, choices=RESOURCE_TYPE_CHOICES)
    
    file = models.FileField(upload_to='resources/', blank=True)
    external_url = models.URLField(blank=True, help_text="If resource is hosted externally")
    
    thumbnail = models.ImageField(upload_to='resources/thumbnails/', blank=True)
    
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self) -> str:
        return self.title





class DonationOption(models.Model):
    """Different donation tiers or options available"""
    title = models.CharField(max_length=160)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = RichTextField()
    impact = models.CharField(max_length=200, blank=True, help_text="e.g., 'Provides training for 5 students'")
    icon = models.CharField(max_length=100, blank=True, help_text="Font Awesome icon class")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self) -> str:
        return self.title

