from __future__ import annotations

from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm, PartnerProposalForm, VolunteerApplicationForm


def _send_form_email(*, subject: str, message: str, from_email: str | None = None) -> None:
    """Send a notification email for engagement forms."""
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email or getattr(settings, "DEFAULT_FROM_EMAIL", None) or settings.SERVER_EMAIL,
        recipient_list=[settings.AFRIETHICS_INFO_EMAIL],
        fail_silently=False,
    )


class ContactView(FormView):
    template_name = "engagement/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("engagement:contact")

    def form_valid(self, form):
        form.save()
        _send_form_email(
            subject="AfriEthics contact form submission",
            message=(
                f"New contact submission\n\n"
                f"Name: {form.cleaned_data.get('name')}\n"
                f"Email: {form.cleaned_data.get('email')}\n"
                f"Phone: {form.cleaned_data.get('phone')}\n\n"
                f"Message:\n{form.cleaned_data.get('message')}\n"
            ),
        )
        messages.success(self.request, "Thanks — your message has been received.")
        return super().form_valid(form)


class VolunteerView(FormView):
    template_name = "engagement/volunteer.html"
    form_class = VolunteerApplicationForm
    success_url = reverse_lazy("engagement:volunteer")

    def form_valid(self, form):
        form.save()
        _send_form_email(
            subject="AfriEthics volunteer application submission",
            message=(
                f"New volunteer application\n\n"
                f"Full name: {form.cleaned_data.get('full_name')}\n"
                f"Email: {form.cleaned_data.get('email')}\n"
                f"Phone: {form.cleaned_data.get('phone_number')}\n"
                f"Area of interest: {form.cleaned_data.get('area_of_interest')}\n\n"
                f"Motivation:\n{form.cleaned_data.get('motivation')}\n"
            ),
        )
        messages.success(self.request, "Thanks — your application has been submitted.")
        return super().form_valid(form)


class PartnerView(FormView):
    template_name = "engagement/partner.html"
    form_class = PartnerProposalForm
    success_url = reverse_lazy("engagement:partner")

    def form_valid(self, form):
        form.save()
        _send_form_email(
            subject="AfriEthics partner proposal submission",
            message=(
                f"New partner proposal\n\n"
                f"Organization: {form.cleaned_data.get('organization_name')}\n"
                f"Contact person: {form.cleaned_data.get('contact_person')}\n"
                f"Email: {form.cleaned_data.get('email')}\n"
                f"Phone: {form.cleaned_data.get('phone_number')}\n"
                f"Collaboration type: {form.cleaned_data.get('collaboration_type')}\n\n"
                f"Message:\n{form.cleaned_data.get('message')}\n"
            ),
        )
        messages.success(self.request, "Thanks — your proposal has been submitted.")
        return super().form_valid(form)


class DonateView(TemplateView):
    template_name = "engagement/donate.html"
