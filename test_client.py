#!/usr/bin/env python
import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "afriethics.settings")
sys.path.insert(0, os.path.dirname(__file__))
django.setup()

from django.test import Client

client = Client()
try:
    response = client.get('/', HTTP_HOST='localhost')
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("SUCCESS: Page loaded successfully!")
    else:
        print(f"Response (first 2000 chars): {response.content[:2000].decode('utf-8', errors='ignore')}")
except Exception as e:
    print(f"Error: {type(e).__name__}")
    print(f"Message: {str(e)}")
    import traceback
    traceback.print_exc()
