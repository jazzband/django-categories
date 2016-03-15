# Django settings for sample project.
import os
import sys
import django

APP = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PROJ_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, APP)
DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'categories',
    'categories.editor',
    'mptt',
    'simpletext',
)

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = os.path.abspath(os.path.join(PROJ_ROOT, 'media', 'uploads'))

MEDIA_URL = '/uploads/'

STATIC_ROOT = os.path.abspath(os.path.join(PROJ_ROOT, 'media', 'static'))

STATIC_URL = '/static/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'bwq#m)-zsey-fs)0#4*o=2z(v5g!ei=zytl9t-1hesh4b&-u^d'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))],
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        }
    }
]

CATEGORIES_SETTINGS = {
    'ALLOW_SLUG_CHANGE': True,
    'RELATION_MODELS': ['simpletext.simpletext', 'flatpages.flatpage'],
    'FK_REGISTRY': {
        'flatpages.flatpage': 'category',
        'simpletext.simpletext': (
            'primary_category',
            {'name': 'secondary_category', 'related_name': 'simpletext_sec_cat'},
        ),
    },
    'M2M_REGISTRY': {
        'simpletext.simpletext': {'name': 'categories', 'related_name': 'm2mcats'},
        'flatpages.flatpage': (
            {'name': 'other_categories', 'related_name': 'other_cats'},
            {'name': 'more_categories', 'related_name': 'more_cats'},
        ),
    },
}

if django.VERSION[1] > 5:
    TEST_RUNNER = 'django.test.runner.DiscoverRunner'
