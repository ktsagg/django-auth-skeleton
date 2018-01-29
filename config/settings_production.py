from .settings_base import *
import os


SECRET_KEY = '&y725w5#_y^bt^30z-j9p+xsbq(b82mrri776yzwc5u%3v)o=j'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'ktsagg.pythonanywhere.com']

INSTALLED_APPS += []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


