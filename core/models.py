from __future__ import annotations

from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


BANNER_TYPE = (
	('banner1', 'banner1'),
	('banner2', 'banner2'),
	('banner3', 'banner3'),
	('banner4', 'banner4'),
	('banner5', 'banner5'),
	('banner6', 'banner6'),
	('banner7', 'banner7'),
	('banner8', 'banner8'),
)

class Banner(models.Model):
	title = models.CharField(max_length=100)
	caption1 = models.CharField(max_length=500, blank=True, null=True)
	caption2 = models.CharField(max_length=500, blank=True, null=True)
	caption3 = models.CharField(max_length=500, blank=True, null=True)
	call_to_text = models.CharField(max_length=500, default="Shop Now")
	call_to_url = models.CharField(max_length=500, default="/")
	image = models.ImageField(upload_to = 'banner/')
	banner_type = models.CharField(max_length=50, default='Top', choices=BANNER_TYPE)
	active = models.BooleanField(default=True)

	def ImageUrl(self):
		if self.image:
			return self.image.url
		else:
			return ""
	def image_tag(self):
		if self.image:
			return mark_safe('<img src="{}" height="70" width="60" />'.format(self.image.url))
		return ""
	image_tag.short_description = 'Image'

	def __str__(self):
		return self.title


class SiteConfiguration(models.Model):
	name = models.CharField(max_length=255, default='Ginamara')
	phone = models.CharField(max_length=20, default = 1, blank=True, null=True)
	phone1 = models.CharField(max_length=20, default = 1, blank=True, null=True)
	phone2 = models.CharField(max_length=20, default = 1, blank=True, null=True)
	phone3 = models.CharField(max_length=20, default = 1, blank=True, null=True)
	logo = models.ImageField(upload_to='config/', default = 'default/Ginamara.png')
	address=models.CharField(max_length=200, default = 'Kampala')
	email = models.EmailField(blank=True, null=True)
	twitter = models.URLField(default = 'twitter.com')
	facebook = models.URLField(default = 'facebook.com')
	youtube = models.URLField(default = 'youtube.com')
	instagram = models.URLField(default = 'instagram.com')
	favicon = models.ImageField(upload_to='config/',  default = 'default/Ajoreb.png')
	banner1 = models.ForeignKey(Banner, on_delete = models.DO_NOTHING, blank=True, null=True, related_name='banner1')
	banner2 = models.ForeignKey(Banner, on_delete = models.DO_NOTHING, blank=True, null=True, related_name='banner2')
	banner3 = models.ForeignKey(Banner, on_delete = models.DO_NOTHING, blank=True, null=True, related_name='banner3')
	banner4 = models.ForeignKey(Banner, on_delete = models.DO_NOTHING, blank=True, null=True, related_name='banner4')
	banner5 = models.ForeignKey(Banner, on_delete = models.DO_NOTHING, blank=True, null=True, related_name='banner5')
	banner6 = models.ForeignKey(Banner, on_delete = models.DO_NOTHING, blank=True, null=True, related_name='banner6')
	banner7 = models.ForeignKey(Banner, on_delete = models.DO_NOTHING, blank=True, null=True, related_name='banner7')
	banner8 = models.ForeignKey(Banner, on_delete = models.DO_NOTHING, blank=True, null=True, related_name='banner8')
	maintenance_mode = models.BooleanField(default=False)

	def __str__(self):
		return "Site Configuration"

	class Meta:
		verbose_name = "Site Configuration"

class Links(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	link = models.URLField()

	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Links"

class FooterLinks(models.Model):
	active = models.BooleanField(default=True)
	is_footer = models.BooleanField(default=False)
	section_name = models.CharField(max_length=200)
	icon = models.CharField(max_length=50, blank=True, null=True)
	links = models.ManyToManyField(Links)

	class Meta:
		verbose_name_plural = "FooterLinks" 
  

class NavigationLink(models.Model):
    label = models.CharField(max_length=60)
    url = models.CharField(max_length=200, help_text="Can be a path like /about/ or a full URL")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "label"]

    def __str__(self) -> str:
        return self.label


class FocusArea(models.Model):
    """Key focus areas of AfriEthics Initiative"""
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=100, blank=True, help_text="Font Awesome icon class")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name_plural = "Focus Areas"

    def __str__(self) -> str:
        return self.name


class ImpactMetric(models.Model):
    """Track impact statistics like people reached, trainings conducted, campaigns launched"""
    name = models.CharField(max_length=120, help_text="e.g., 'People Reached', 'Trainings Conducted'")
    value = models.CharField(max_length=100, help_text="e.g., '10,000+' or '250'")
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=100, blank=True, help_text="Font Awesome icon class")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self) -> str:
        return f"{self.name}: {self.value}"


# Alias for backwards compatibility
SiteSettings = SiteConfiguration

