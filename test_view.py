#!/usr/bin/env python
import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "afriethis.settings")
sys.path.insert(0, os.path.dirname(__file__))
django.setup()

from django.test import RequestFactory
from core.views import HomeView

factory = RequestFactory()
request = factory.get('/')
view = HomeView.as_view()

try:
    response = view(request)
    print(f"Status Code: {response.status_code}")
    if response.status_code != 200:
        print(f"Response: {response.content[:500]}")
except Exception as e:
    print(f"Error: {type(e).__name__}")
    print(f"Message: {str(e)}")
    import traceback
    traceback.print_exc()
