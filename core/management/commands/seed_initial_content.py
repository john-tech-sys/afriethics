from __future__ import annotations

from django.core.management.base import BaseCommand

from blog.models import Post
from core.models import NavigationLink, SiteSettings
from home.models import HomepageHeroSlide, Page
from programs.models import Program


class Command(BaseCommand):
    help = "Seed initial content for local development"

    def handle(self, *args, **options):
        settings, _ = SiteSettings.objects.get_or_create(
            id=1,
            defaults={
                "site_name": "AfriEthics Initiative",
                "tagline": "Rooted in Values. Rising with purpose",
                "email": "info@afriethics.org",
            },
        )
        self.stdout.write(self.style.SUCCESS(f"SiteSettings: {settings.site_name}"))

        nav_defaults = [
            ("About", "/about/", 10),
            ("Activities", "/programs/", 20),
            ("Blog", "/blog/", 30),
            ("Team", "/team/", 40),
            ("Contact", "/contact/", 50),
            ("Donate", "/donate/", 60),
        ]
        for label, url, order in nav_defaults:
            NavigationLink.objects.get_or_create(label=label, defaults={"url": url, "order": order})

        Page.objects.get_or_create(
            slug="about",
            defaults={
                "title": "About Us",
                "summary": (
                    "The AfriEthics Initiative is a nonprofit organization founded by young, experienced, "
                    "and Certified Fraud Examiners (CFEs) with a shared passion for integrity-driven leadership."
                ),
                "body": "<h2>Our Vision</h2><p>To shape an Africa led by a new generation of ethical leaders and institutions anchored in integrity and accountability.</p>"
                "<h2>Our Mission</h2><p>To nurture ethical leadership and responsible citizenship by promoting values-based education, civic engagement, and inclusive development initiatives across the continent.</p>",
                "show_in_nav": True,
                "nav_label": "About",
                "nav_order": 10,
            },
        )

        Page.objects.get_or_create(
            slug="why-we-exist",
            defaults={
                "title": "Why We Exist",
                "summary": "Ethical leadership is the foundation for Africa’s transformation.",
                "body": (
                    "<p>At AfriEthics Initiative, we believe that ethical leadership is not optional — it is the foundation "
                    "for sustainable development, justice, and trust in both public and private institutions.</p>"
                ),
            },
        )

        Page.objects.get_or_create(
            slug="what-we-think",
            defaults={
                "title": "What We Think",
                "summary": "Ethical leadership is the foundation for Africa’s transformation.",
                "body": (
                    "<p>Our work is rooted in values that challenge corruption, inspire integrity, and empower young people to rise with purpose.</p>"
                ),
            },
        )

        HomepageHeroSlide.objects.get_or_create(
            order=10,
            headline="Rooted in Values. Rising with purpose",
            defaults={
                "subheadline": "Ethical principles guide every decision, building trust and fostering respect in all we do.",
                "cta_label": "Learn More",
                "cta_url": "/about/",
                "is_active": True,
            },
        )

        Program.objects.get_or_create(
            slug="values-based-education",
            defaults={
                "title": "Values-based Education",
                "summary": "Promoting ethical thinking and responsible citizenship.",
                "description": "Educational activities designed to nurture integrity and accountability.",
                "order": 10,
                "is_published": True,
            },
        )

        Post.objects.get_or_create(
            slug="why-uganda-cant-afford-corruption",
            defaults={
                "title": "Why Uganda Can’t Afford Corruption",
                "excerpt": "Uganda loses UGX 10 trillion to corruption every year — a loss that harms the most vulnerable.",
                "content": (
                    "<p><strong>Opening:</strong> Uganda loses UGX 10 trillion to corruption every year, equivalent to over 44% of national revenue.</p>"
                    "<p><strong>Story:</strong> Corruption isn’t just numbers — it’s lost futures, broken communities, and shattered dreams.</p>"
                    "<p><strong>Call to Action:</strong> You can help us raise the next generation of ethical leaders by volunteering.</p>"
                ),
                "status": Post.Status.PUBLISHED,
            },
        )

        self.stdout.write(self.style.SUCCESS("Seed complete."))
