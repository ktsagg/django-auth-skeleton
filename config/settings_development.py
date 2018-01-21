from .settings_base import *
import os

SECRET_KEY = '&y795w5#_y^bt^30z-j9p+xscq(a82mrri776yzwc5u%3v)o=c'

DEBUG = True

ALLOWED_HOSTS = []

# Debug-toolbar Settings ######################################################
INSTALLED_APPS += ['debug_toolbar', ]
INTERNAL_IPS = ['127.0.0.1', 'localhost', ]
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



