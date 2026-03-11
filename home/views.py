from django.shortcuts import render

from config.models import Document, HeaderLinks
from contrib.models import Partner
from ginamara import settings
from home.forms import ApplicationForm
from home.models import *
from noticeboard.models import Faq, News
from services.models import AboutIntern, Internship, Service

# Create your views here.

def index(request):
    menu = HeaderLinks.objects.all()  
    # news = News.objects.all()[:3]  
    domestic = AboutIntern.objects.filter(is_domestic=True)    
    international = AboutIntern.objects.filter(is_domestic=False)
    # served = HappyCustomers.objects.all()[:4]
    services = Service.objects.all()  
    faqs = Faq.objects.all().order_by('id')[:3]
    # internships = Internship.objects.filter(active=True)[:6]
    context = {
        'services': services,
        # 'data': internships,
        'faqs': faqs,
        'menu': menu,
        # 'served': served,
        'international': international,
        'domestic': domestic,
    }	
    context['segment'] = 'home'
    return render(request, 'home/index.html', context)

def apply_for_cert(request):
    processes = Process.objects.filter(is_intern=False).order_by('number')

    context = { 'processes': processes}
    context['segment'] = 'certification'
    return render(request, 'home/apply_for_cert.html', context)


def apply(request):
    processes = Process.objects.filter(is_intern=True).order_by('number')
    documents = Document.objects.filter(is_intern=True)

    context = { 
               'processes': processes,
               'documents': documents
               }
    context['segment'] = 'internship'
    return render(request, 'home/apply.html', context)


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
