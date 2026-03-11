from django.urls import path

from .views import ContactView, DonateView, PartnerView, VolunteerView

app_name = "engagement"

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact"),
    path("donate/", DonateView.as_view(), name="donate"),
    path("volunteer/", VolunteerView.as_view(), name="volunteer"),
    path("partner/", PartnerView.as_view(), name="partner"),
]

