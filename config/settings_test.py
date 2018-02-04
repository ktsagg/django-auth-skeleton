from .settings_base import *
import os


SECRET_KEY = '&y795w5#_y^bt^30z-j9p+xscq(a82mrri776yzwc5u%3v)o=c'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Tell Web Server to look for static files in /some/directory/
# Then you run "manage.py collectstatic" and Django will copy static files from all the apps
# and from the directories defined in STATICFILES_DIRS to /some/directory/.

# STATIC_ROOT = '/some/directory/'
