from __future__ import annotations

from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import ContactForm, PartnerProposalForm, VolunteerApplicationForm


class ContactView(FormView):
    template_name = "engagement/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("engagement:contact")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Thanks — your message has been received.")
        return super().form_valid(form)


class VolunteerView(FormView):
    template_name = "engagement/volunteer.html"
    form_class = VolunteerApplicationForm
    success_url = reverse_lazy("engagement:volunteer")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Thanks — your application has been submitted.")
        return super().form_valid(form)


class PartnerView(FormView):
    template_name = "engagement/partner.html"
    form_class = PartnerProposalForm
    success_url = reverse_lazy("engagement:partner")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Thanks — your proposal has been submitted.")
        return super().form_valid(form)


class DonateView(TemplateView):
    template_name = "engagement/donate.html"
