# -*- coding: utf-8 -*-
from django.urls import path

from .views import home, about, docs, faq, privacy

urlpatterns = [
  path('', home, name="home"),
  path('about', about, name="about"),
  path('docs', docs, name="docs"),
  path('faq', faq, name="faq"),
  path('privacy', privacy, name="privacy"),
]
