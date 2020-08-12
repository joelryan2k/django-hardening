from django.urls import path

from .views import csp_report

app_name = "hardening"

urlpatterns = [
    path("csp-report/", csp_report, name="csp-report",),
]
