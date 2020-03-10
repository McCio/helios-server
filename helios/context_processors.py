from django.conf import settings as django_settings

__all__ = ('settings',)


def settings(request):
    return {'settings': django_settings}
