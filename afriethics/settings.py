"""Django settings for afriethics project.

Generated manually (Django-like defaults) for this repository.

For more information on this file, see
https://docs.djangoproject.com/en/stable/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/stable/ref/settings/
"""

from __future__ import annotations

import os, mimetypes
from pathlib import Path
from decouple import config, Csv
import dj_database_url
import environ

mimetypes.add_type("text/css", ".css", True)

# mimetypes.add_type("text/js", ".js", True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ENVIRONMENT = config('ENVIRONMENT', default='production')
# SECURITY WARNING: don't run with debug turned on in production!
if ENVIRONMENT == 'development':
    DEBUG = True
else:
    DEBUG = False
    
env = environ.Env(
    DJANGO_DEBUG=(bool, True),
)

if env.bool("DJANGO_READ_DOT_ENV", default=False):
    env.read_env(BASE_DIR / ".env")

# SECURITY WARNING: keep the secret key used in production secret!
# Prefer setting DJANGO_SECRET_KEY in your environment (or a .env you load externally).
SECRET_KEY = env("DJANGO_SECRET_KEY", default="change-me")

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'afriethics.onrender.com', 'afriethics.org', 'www.afriethics.org']

CSRF_TRUSTED_ORIGINS = ['https://afriethics.onrender.com', 'https://afriethics.org', 'https://www.afriethics.org']


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    'storages',
    "ckeditor",

    "core",
    "home",
    "programs",
    "people",
    "blog",
    "engagement",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "afriethics.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core.context_processors.site_context",
            ],
        },
    }
]

WSGI_APPLICATION = "afriethics.wsgi.application"
ASGI_APPLICATION = "afriethics.asgi.application"


# DATABASES = {
#     'default': dj_database_url.config(default='sqlite:///db.sqlite3')
# }

# DATABASES = {
#     "default": dj_database_url.config(
#         default=f"sqlite:///{(BASE_DIR / 'db.sqlite3').as_posix()}",
#         conn_max_age=600,
#         conn_health_checks=True,
#     )
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

POSTGRES_LOCALLY = True

if ENVIRONMENT == 'production' or POSTGRES_LOCALLY == True:
    DATABASES['default'] = dj_database_url.parse(config('DATABASE_URL'))
    

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


TEMP = os.path.join(BASE_DIR, 'media/temp')

CKEDITOR_UPLOAD_PATH = "uploads/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"




AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = config("AWS_S3_ENDPOINT_URL")          # e.g. https://xxx.r2.cloudflarestorage.com
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_S3_ADDRESSING_STYLE = "virtual"
AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = "public-read"
AWS_S3_REGION_NAME = "auto"          # Important for R2

# Public URL (highly recommended)
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.r2.cloudflarestorage.com"   # or your custom domain

# Folder paths inside the bucket
AWS_LOCATION = "media"
STATIC_LOCATION = "static"

# ====================== STORAGE BACKENDS ======================

# if ENVIRONMENT == 'development':
    # Local storage for development
# STATIC_URL = "/static/"
# MEDIA_URL = "/media/"
# STATICFILES_DIRS = [BASE_DIR / "static"]
# STATIC_ROOT = BASE_DIR / "staticfiles"
# MEDIA_ROOT = BASE_DIR / "media"

if ENVIRONMENT == 'development':
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }

else:
    # Production: Cloudflare R2
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3.S3Storage",   # or your custom if needed
            "OPTIONS": {
                "location": AWS_LOCATION,
            },
        },
        "staticfiles": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {
                "location": STATIC_LOCATION,
            },
        },
    }

#     STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/"
#     MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"



# Storage configuration used by Django 4.2+.
# STORAGES = {
#     "default": {
#         "BACKEND": "helpers.cloudflare.storages.MediaFilesStorage",  # Media files storage
#     },
#     "staticfiles": {
#         "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
#     },
# }
# URL to access static files (adjust to your Cloudflare R2 bucket)
STATIC_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/static/"

# URL to access media files

MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/media/"


# Email (defaults to console; configure SMTP via env vars in production)
EMAIL_BACKEND = env("DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")

# Common security toggles (safe defaults for many PaaS deployments)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True