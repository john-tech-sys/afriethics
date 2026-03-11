

from django import forms

from contrib.models import Apply
from services.models import Internship
from .models import *


class ApplicationForm(forms.ModelForm):
	class Meta:
		model = Apply
		fields = ('study_country', 'phone', 'email', 'message', 'nationality', 'first_name', 'last_name', 'accept_terms')


class InternFilterForm(forms.ModelForm):
    class Meta:
        model  = Internship
        fields = ['location', 'salary', 'languages', 'work_type']

