from django.shortcuts import render

from home.forms import ApplicationForm
from home.models import *
# Create your views here.

def apply_for_cert(request):
    processes = Process.objects.filter(is_intern=False).order_by('number')

    context = { 'processes': processes}
    context['segment'] = 'certification'
    return render(request, 'home/apply_for_cert.html', context)


def error(request):
    return render(request, 'home/error.html', )


def partnership(request):
    partner = Partnership.objects.first()
    whys = WhyPartnerWithUs.objects.all()
    areas = AreasOfPartnership.objects.all()
    context = {
        'partner': partner,
        'whys': whys,
        'areas': areas,
    }
    context['segment'] = 'partnership'
    return render(request, 'home/partnership.html', context)
