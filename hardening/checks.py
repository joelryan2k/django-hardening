import pkg_resources

from django.core.checks import Error, register
from django.conf import settings

@register()
def check_axes_config(app_configs, **kwargs):
    errors = []
    
    axes_version = pkg_resources.get_distribution("django-axes").version

    if axes_version != '5.4.3':
        errors.append(
            Error(
                'axes must be installed',
                hint='Install django-axes',
                obj=None,
                id='hardening.E004',
            )
        )

    if 'axes' not in settings.INSTALLED_APPS:
        errors.append(
            Error(
                'axes must be in INSTALLED_APPS',
                hint='Add django axes to list of installed apps and configure',
                obj=None,
                id='hardening.E001',
            )
        )

    if settings.AUTHENTICATION_BACKENDS[0] != 'axes.backends.AxesBackend':
        errors.append(
            Error(
                'axes must be the first authentication backend',
                hint='Add "axes.backends.AxesBackend" as the first entry in AUTHENTICATION_BACKENDS',
                obj=None,
                id='hardening.E002',
            )
        )

    if len(settings.MIDDLEWARE) == 0 or settings.MIDDLEWARE[len(settings.MIDDLEWARE) - 1] != 'axes.middleware.AxesMiddleware':
        errors.append(
            Error(
                'axes must be the last middleware entry',
                hint='Add "axes.middleware.AxesMiddleware" as the last entry in MIDDLEWARE',
                obj=None,
                id='hardening.E003',
            )
        )

    return errors

@register()
def check_csp_config(app_configs, **kwargs):
    errors = []
    
    csp_version = pkg_resources.get_distribution("django_csp").version

    if csp_version != '3.6':
        errors.append(
            Error(
                'csp must be installed',
                hint='Install django-csp',
                obj=None,
                id='hardening.E005',
            )
        )

    if 'csp.middleware.CSPMiddleware' not in settings.MIDDLEWARE:
        errors.append(
            Error(
                'csp.middleware.CSPMiddleware must be in MIDDLEWARE',
                hint='Add "csp.middleware.CSPMiddleware" to MIDDLEWARE',
                obj=None,
                id='hardening.E006',
            )
        )

    if not hasattr(settings, 'CSP_FRAME_ANCESTORS') or not settings.CSP_FRAME_ANCESTORS:
        errors.append(
            Error(
                'CSP_FRAME_ANCESTORS must be True',
                hint='Set CSP_FRAME_ANCESTORS to True in settings.py',
                obj=None,
                id='hardening.E016',
            )
        )

    return errors

@register()
def check_django_config(app_configs, **kwargs):
    errors = []

    if 'django.middleware.csrf.CsrfViewMiddleware' not in settings.MIDDLEWARE:
        errors.append(
            Error(
                'django.middleware.csrf.CsrfViewMiddleware must be in MIDDLEWARE',
                hint='Add "django.middleware.csrf.CsrfViewMiddleware" to MIDDLEWARE',
                obj=None,
                id='hardening.E007',
            )
        )

    if 'django.middleware.clickjacking.XFrameOptionsMiddleware' not in settings.MIDDLEWARE:
        errors.append(
            Error(
                'django.middleware.clickjacking.XFrameOptionsMiddleware must be in MIDDLEWARE',
                hint='Add "django.middleware.clickjacking.XFrameOptionsMiddleware" to MIDDLEWARE',
                obj=None,
                id='hardening.E008',
            )
        )

    if not settings.SESSION_COOKIE_SECURE:
        errors.append(
            Error(
                'SESSION_COOKIE_SECURE must be True',
                hint='Set SESSION_COOKIE_SECURE to True in settings.py',
                obj=None,
                id='hardening.E009',
            )
        )

    if not settings.CSRF_COOKIE_SECURE:
        errors.append(
            Error(
                'CSRF_COOKIE_SECURE must be True',
                hint='Set CSRF_COOKIE_SECURE to True in settings.py',
                obj=None,
                id='hardening.E010',
            )
        )

    if 'django.middleware.security.SecurityMiddleware' not in settings.MIDDLEWARE:
        errors.append(
            Error(
                'django.middleware.security.SecurityMiddleware must be in MIDDLEWARE',
                hint='Add "django.middleware.security.SecurityMiddleware" to MIDDLEWARE',
                obj=None,
                id='hardening.E011',
            )
        )

    if not settings.SECURE_CONTENT_TYPE_NOSNIFF:
        errors.append(
            Error(
                'SECURE_CONTENT_TYPE_NOSNIFF must be True',
                hint='Set SECURE_CONTENT_TYPE_NOSNIFF to True in settings.py',
                obj=None,
                id='hardening.E012',
            )
        )

    if not settings.SECURE_SSL_REDIRECT:
        errors.append(
            Error(
                'SECURE_SSL_REDIRECT must be True',
                hint='Set SECURE_SSL_REDIRECT to True in settings.py',
                obj=None,
                id='hardening.E013',
            )
        )

    if settings.CSRF_COOKIE_SAMESITE != 'Strict':
        errors.append(
            Error(
                'CSRF_COOKIE_SAMESITE must be "Strict"',
                hint='Set CSRF_COOKIE_SAMESITE to "Strict" in settings.py',
                obj=None,
                id='hardening.E014',
            )
        )

    if settings.SESSION_COOKIE_SAMESITE != 'Strict':
        errors.append(
            Error(
                'SESSION_COOKIE_SAMESITE must be "Strict"',
                hint='Set SESSION_COOKIE_SAMESITE to "Strict" in settings.py',
                obj=None,
                id='hardening.E015',
            )
        )

    return errors
