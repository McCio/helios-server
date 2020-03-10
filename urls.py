# -*- coding: utf-8 -*-
from django.conf import settings
from django.urls import path, include
from django.views.static import serve


def __static(base):
    return base + '<path:path>'


urlpatterns = [
    path('auth/', include('helios_auth.urls')),
    path('helios/', include('helios.urls')),

    # SHOULD BE REPLACED BY APACHE STATIC PATH
    path(__static(settings.BOOTH_STATIC_URL), serve, {'document_root': settings.BOOTH_STATIC_ROOT}),
    path(__static(settings.VERIFIER_STATIC_URL), serve, {'document_root': settings.VERIFIER_STATIC_ROOT}),

    path(__static(settings.AUTH_STATIC_URL), serve, {'document_root': settings.AUTH_STATIC_ROOT}),
    path(__static(settings.HELIOS_STATIC_URL), serve, {'document_root': settings.HELIOS_STATIC_ROOT}),
    path(__static(settings.BASE_STATIC_URL), serve, {'document_root': settings.BASE_STATIC_ROOT}),

    path('', include('server_ui.urls')),
]
