"""Django settings for afriethics project.

Generated manually (Django-like defaults) for this repository.

For more information on this file, see
https://docs.djangoproject.com/en/stable/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/stable/ref/settings/
"""

from __future__ import annotations

import os
from pathlib import Path

import dj_database_url
import environ


BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DJANGO_DEBUG=(bool, True),
)

if env.bool("DJANGO_READ_DOT_ENV", default=False):
    env.read_env(BASE_DIR / ".env")

# SECURITY WARNING: keep the secret key used in production secret!
# Prefer setting DJANGO_SECRET_KEY in your environment (or a .env you load externally).
SECRET_KEY = env("DJANGO_SECRET_KEY", default="change-me")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", default=False)

# Comma-separated hostnames, e.g. "example.com,.example.com,localhost,127.0.0.1"
raw_allowed_hosts = env("DJANGO_ALLOWED_HOSTS", default="localhost,127.0.0.1")
# ALLOWED_HOSTS = [h.strip() for h in raw_allowed_hosts.split(",") if h.strip()]
ALLOWED_HOSTS = ['*']  # later you can restrict
raw_csrf_trusted = env("DJANGO_CSRF_TRUSTED_ORIGINS", default="")
CSRF_TRUSTED_ORIGINS = [o.strip() for o in raw_csrf_trusted.split(",") if o.strip()]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

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

DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{(BASE_DIR / 'db.sqlite3').as_posix()}",
        conn_max_age=600,
        conn_health_checks=True,
    )
}


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

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

TEMP = os.path.join(BASE_DIR, 'media/temp')

CKEDITOR_UPLOAD_PATH = "uploads/"

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email (defaults to console; configure SMTP via env vars in production)
EMAIL_BACKEND = env("DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")

# Common security toggles (safe defaults for many PaaS deployments)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True