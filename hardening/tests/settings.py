from __future__ import unicode_literals

import environ

env = environ.Env()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:"
    },
}

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "axes",
    "csp",
    "tests.testapp.apps.TestAppConfig"
]

SITE_ID = 1

SECRET_KEY = "test"

MIDDLEWARE = [
    "csp.middleware.CSPMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "axes.middleware.AxesMiddleware",
]

AUTHENTICATION_BACKENDS = [
    "axes.backends.AxesBackend",
    "django.contrib.auth.backends.ModelBackend",
]

ROOT_URLCONF = 'urls'

AXES_META_PRECEDENCE_ORDER = [
    "HTTP_X_FORWARDED_FOR",
]
