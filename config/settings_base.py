"""
Django settings for _config project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'aon5^n61l(s@5&j&=gl-qzif3nalw^_owfh9prky!4mo*g(w)('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition ######################################################
INSTALLED_APPS = [
    # Default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Extra django apps
    'django.contrib.admindocs',
    'django.forms',  # required for custom widjets

    # 3rd party apps
    'widget_tweaks',

    # Project's apps
    'apps.home.apps.HomeConfig',
    'apps.accounts.apps.AccountsConfig',
]


###############################################################################
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


###############################################################################
ROOT_URLCONF = 'config.urls'


# Teplates ####################################################################
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # put your templates here
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

            # No registration needed if we store the custom tags in:
            # <application-name>/templatetags/<module-name>.py
            # Also create an __init__.py, so django is able to load modules.

            # Registering the template-tags modules
            'libraries': {
                'form_tags': 'template_tags.form_tags',
            },
        },
    },
]


# Web Server Gateway Interface ################################################
WSGI_APPLICATION = 'config.wsgi.application'


# Database ####################################################################
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases ###############
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation #########################################################
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators#
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization ########################################################
# https://docs.djangoproject.com/en/2.0/topics/i18n/ ##########################
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) ######################################
# https://docs.djangoproject.com/en/2.0/howto/static-files/ ###################
STATIC_URL = '/static/'

# store your static files here
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


# Auth Backends ###############################################################
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend',  # by default
                           'apps.accounts.backends.EmailBackend']  # supports user login by email


# Login Variables #############################################################
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'


#
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Required for custom widjets
FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'
