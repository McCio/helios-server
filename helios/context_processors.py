from django.conf import settings as django_settings

__all__ = ('settings', 'current_url',)


def settings(request):
    return {'settings': django_settings}


def current_url(request):
    return {'CURRENT_URL': request.path}
