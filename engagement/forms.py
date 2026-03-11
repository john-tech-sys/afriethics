from __future__ import annotations

from django import forms

from .models import ContactMessage, PartnerProposal, VolunteerApplication


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }


class VolunteerApplicationForm(forms.ModelForm):
    class Meta:
        model = VolunteerApplication
        fields = ["full_name", "email", "phone_number", "area_of_interest", "motivation"]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "area_of_interest": forms.TextInput(attrs={"class": "form-control"}),
            "motivation": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }


class PartnerProposalForm(forms.ModelForm):
    class Meta:
        model = PartnerProposal
        fields = [
            "organization_name",
            "contact_person",
            "email",
            "phone_number",
            "collaboration_type",
            "message",
        ]
        widgets = {
            "organization_name": forms.TextInput(attrs={"class": "form-control"}),
            "contact_person": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "collaboration_type": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 6}),
        }
