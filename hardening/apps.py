from django.apps import AppConfig

class DjangoHardeningConfig(AppConfig):
    name = 'hardening'

    def ready(self):
        import hardening.checks
