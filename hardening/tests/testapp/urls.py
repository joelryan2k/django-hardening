from django.urls import include, path
from django.conf.urls import url
from django.conf import settings

urlpatterns = []

urlpatterns.append(url(r"^hardening/", include("hardening.urls", namespace="hardening")))
