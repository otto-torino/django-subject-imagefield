# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

default_config = {
    'PREVIEW_WIDTH': 300
}


def get_config(key):
    user_settings = getattr(settings, 'SUBJECT_IMAGEFIELD', None)

    if user_settings is None:
        value = default_config.get(key, None)
    else:
        value = user_settings.get(key, default_config.get(key, None))

    if not isinstance(value, int):
        raise ImproperlyConfigured('PREVIEW_WIDTH setting must be an integer')

    return value
