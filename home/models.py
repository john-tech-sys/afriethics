from django.urls import reverse

from autoslug import AutoSlugField
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from afriethics import settings
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
        return self.vision or "Unnamed Ethos"

    class Meta:
        verbose_name_plural = "Ethos"


class Values(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    call_to_url = models.CharField(max_length=500, default="/")
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or "Unnamed Value"

    class Meta:
        ordering = ["order", "title"]
        verbose_name_plural = "Values"


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


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


class IntroVideo(models.Model):
    """Pitch / introductory video shown on the homepage."""

    title = models.CharField(max_length=160, default="Watch Our Story")
    subtitle = models.CharField(max_length=255, blank=True, help_text="Short line shown below the title")
    # Admins paste an embed URL (YouTube: https://www.youtube.com/embed/ID, Vimeo: https://player.vimeo.com/video/ID)
    embed_url = models.URLField(
        blank=True,
        help_text="YouTube or Vimeo embed URL (e.g. https://www.youtube.com/embed/xxxxx)",
    )
    # Alternative: an uploaded video file
    video_file = models.FileField(
        upload_to="intro_videos/",
        blank=True,
        help_text="Upload an MP4 file (used when no embed URL is provided)",
    )
    thumbnail = models.ImageField(
        upload_to="intro_videos/thumbs/",
        blank=True,
        help_text="Poster image shown before the video plays",
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Intro / Pitch Video"
        verbose_name_plural = "Intro / Pitch Videos"

    def __str__(self) -> str:
        return self.title


class ProblemPage(models.Model):
    """Database-driven content for the Why We Exist / Problem page.

    All of the text, statistics, links and call-to-action elements on the
    problem page are editable through this singleton model.
    """

    # ── Hero / intro section ──────────────────────────────────────────
    badge_text = models.CharField(
        max_length=150,
        default="Why We Exist",
        help_text="Small pill / badge shown above the heading",
    )
    section_title = models.CharField(
        max_length=300,
        default="Ethical Leadership is the Foundation for Africa's Transformation",
        help_text="Main heading of the page",
    )
    intro_description = models.TextField(
        blank=True,
        help_text="Introductory paragraph below the main heading.",
    )

    # ── Challenge block ───────────────────────────────────────────────
    challenge_title = models.CharField(
        max_length=300,
        default="The Challenge of Corruption in Uganda",
        help_text="Title of the challenge / statistics section",
    )
    challenge_body = RichTextField(
        blank=True,
        help_text=(
            "Main body text with corruption statistics. "
            "Use the rich-text editor to format paragraphs, bold numbers, etc."
        ),
    )

    # ── Source attribution ────────────────────────────────────────────
    source_label = models.CharField(
        max_length=500,
        blank=True,
        help_text="Visible text of the source link (e.g. 'Uganda Inspectorate of Government (IGG)')",
    )
    source_url = models.URLField(
        blank=True,
        help_text="URL the source label should link to",
    )

    # ── Closing statement ─────────────────────────────────────────────
    closing_statement = RichTextField(
        blank=True,
        help_text="Bold statement that appears below the horizontal rule, explaining why the organisation exists.",
    )

    # ── Call to action ────────────────────────────────────────────────
    cta_header = models.CharField(
        max_length=300,
        blank=True,
        default="This is what we believe.\nIf you believe it too, join us.",
        help_text="Heading above the CTA buttons",
    )
    cta_volunteer_text = models.CharField(
        max_length=100,
        default="Volunteer",
    )
    cta_volunteer_url = models.CharField(
        max_length=500,
        default="/volunteer/",
    )
    cta_partner_text = models.CharField(
        max_length=100,
        default="Partner With Us",
    )
    cta_partner_url = models.CharField(
        max_length=500,
        default="/partner/",
    )
    cta_programs_text = models.CharField(
        max_length=100,
        default="Read Our Work",
    )
    cta_programs_url = models.CharField(
        max_length=500,
        default="/programs/",
    )

    # ── Publishing controls ───────────────────────────────────────────
    is_published = models.BooleanField(
        default=True,
        help_text="Uncheck to hide this content (the page will fall back to defaults).",
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Problem Page"
        verbose_name_plural = "Problem Page"

    def __str__(self) -> str:
        return "Why We Exist – Problem Page"

    def save(self, *args, **kwargs):
        """Ensure only one ProblemPage instance exists (singleton pattern)."""
        if not self.pk and ProblemPage.objects.exists():
            # If an instance already exists, update it instead of creating a new one
            existing = ProblemPage.objects.first()
            self.pk = existing.pk
        super().save(*args, **kwargs)