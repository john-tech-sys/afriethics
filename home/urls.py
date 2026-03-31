from django.urls import path
from .views import *
from django.urls import path



urlpatterns = [
	path('', index, name='home'),
    path("health/", health),
	path('apply_for_cert', apply_for_cert, name='apply_for_cert'),
	path('partnership', partnership, name='partnership'),
	path('apply', apply, name='apply'),
	path('error', error, name='error'),
]