# -*- coding: utf-8 -*-
from django.conf import settings

default_config = {
    'PREVIEW_WIDTH': 300
}


def get_config(key):
    user_settings = getattr(settings, 'SUBJECT_IMAGEFIELD', None)

    if user_settings is None:
        value = default_config.get(key, None)
    else:
        value = user_settings.get(key, default_config.get(key, None))

    return value
