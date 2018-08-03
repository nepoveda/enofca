# -*- coding: utf-8 -*-
from os.path import join
from .base import *

DEBUG=True
ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'OPTIONS': {"charset": "utf8mb4", "init_command": "SET default_storage_engine=InnoDB",},
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'enofca',
        'USER': 'dan',
        'PASSWORD': 'daniking',
        'HOST': 'localhost',
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
