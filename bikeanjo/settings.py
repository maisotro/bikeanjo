# -*- coding: utf-8 -*-
"""
Django settings for bikeanjo project.

Generated by 'django-admin startproject' using Django 1.8b1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import environ
from django.utils.translation import ugettext_lazy as _

env = environ.Env()
root = environ.Path(__file__) - 2
environ.Env.read_env(str(root.path('.env')))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
BASE_DIR = str(root)

ADMINS = (
    ('Fabio Montefuscolo', 'fabio.montefuscolo@hacklab.com.br'),
)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='%1f#2u69h04113465m-7l_bc3456`[]~z@rgkys8zao%zpw9mt(')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=False)
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['*'])

# Application definition
INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.gis',
    'django.contrib.flatpages',
    'django.contrib.postgres',
    'django_extensions',
    'debug_toolbar',
    'filer',
    'easy_thumbnails',
    'rosetta',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
    'djrill',
    'import_export',
    'rest_framework',
    'cities',
    'cyclists',
    'front',
    'emailqueue',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'middlewares.ViewNameMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'middlewares.BikeanjoLocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'middlewares.BikeanjoSessionConfigMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'bikeanjo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(root.path('templates')),
        ],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'bikeanjo.context_processors.bikeconf',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'allauth.account.context_processors.account',
                'allauth.socialaccount.context_processors.socialaccount',
            ],
            'loaders': [
                'bikeanjo.template.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]


# o allauth ainda usa TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS = TEMPLATES[0]['OPTIONS']['context_processors']

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

WSGI_APPLICATION = 'bikeanjo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': env.db("DJANGO_DATABASE_URL", default='postgis://postgis/bikeanjo' ),
}


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = env('DJANGO_LANGUAGE_CODE', default='pt-br')
TIME_ZONE = env('DJANGO_TIME_ZONE', default='America/Sao_Paulo')

USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ('pt-br', _('Brazilian Portuguese')),
    ('es', _('Spanish')),
    ('en', _('English')),
)

LOCALE_PATHS = (
    str(root.path('locale')),
)

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_URL = env('DJANGO_STATIC_URL', default='/static/')
STATIC_ROOT = str(root.path('static'))
STATICFILES_DIRS = env.list('STATICFILES_DIRS', default=[])

MEDIA_URL = env('DJANGO_MEDIA_URL', default='/media/')
MEDIA_ROOT = str(root.path('media'))


SITE_ID = 1

AUTH_USER_MODEL = 'cyclists.User'

ACCOUNT_ADAPTER = 'front.adapters.BikeanjoAccountAdapter'
ACCOUNT_SIGNUP_FORM_CLASS = 'front.forms.SignupForm'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "none"

SOCIALACCOUNT_ADAPTER = 'front.adapters.BikeanjoSocialAccountAdapter'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_AUTO_SIGNUP = False
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email', 'user_birthday',
                  'user_location', 'public_profile'],
        'METHOD': 'js_sdk',
        'VERIFIED_EMAIL': False
    },
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'}
    },
}

LOGIN_REDIRECT_URL = '/'
SESSION_COOKIE_AGE_FOR_INCOMPLETE_REGISTER = 600

EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')

EMAIL_USE_TLS = env('DJANGO_EMAIL_USE_TLS', default=None)
EMAIL_HOST = env('DJANGO_EMAIL_HOST', default=None)
EMAIL_PORT = env('DJANGO_EMAIL_PORT', default=None)
EMAIL_HOST_PASSWORD = env('DJANGO_EMAIL_HOST_PASSWORD', default=None)
EMAIL_HOST_USER = env('DJANGO_EMAIL_HOST_USER', default=None)

DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL', default='Equipe Bike Anjo<noreply@bikeanjo.org>')
DEFAULT_TO_EMAIL = env('DJANGO_DEFAULT_TO_EMAIL', default='Equipe Bike Anjo<contato@bikeanjo.org>')

MANDRILL_API_KEY = env('MANDRILL_API_KEY', default='brack3t-is-awesome')
GOOGLE_ANALYTICS = env('DJANGO_GOOGLE_ANALYTICS', default='')
GOOGLE_SITE_VERIFICATION = env('DJANGO_GOOGLE_SITE_VERIFICATION', default='')

FORMAT_MODULE_PATH = [
    'bikeanjo.formats',
]

try:
    from .settings_local import *
except ImportError:
    pass
