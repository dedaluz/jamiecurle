# Django settings for jamiecurle project.
import os
ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ADMINS = (
     ('Jamie Curle', 'me@jamiecurle.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'jamiecurle2',                      # Or path to database file if using sqlite3.
        'USER': 'jcurle',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Europe/London'

LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

USE_I18N = False

USE_L10N = False

MEDIA_ROOT = path('media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://media.jamiecurle.com/'

INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS' : False
}# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'p42zs_pmv5+daiosqr(7byclz!fyveb)b)vi0ykb(zq+kbz1#f'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'apps.stats.middleware.StatsMiddleware',
    #'johnny.middleware.LocalStoreClearMiddleware',
    #'johnny.middleware.QueryCacheMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'jamiecurle.urls'

TEMPLATE_DIRS = (
    path('templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.markup',
    'disqus',
    'south',
    'debug_toolbar',
    'johnny',
    'taggit',
    'gunicorn',
    'compressor',
    'form_utils',
    'apps.blog',
    'apps.tags',
    'apps.instagram',
    'apps.pinboard',
    'apps.lastfm',
    'apps.twitter',
    'apps.utils',
    'apps.stats',
    'apps.quotes',
)

JOHNNY_MIDDLEWARE_KEY_PREFIX='jamiecurle'
CACHES = {
        'default': {
            'BACKEND': 'johnny.backends.memcached.CacheClass',
            'LOCATION': '127.0.0.1:11211'
        }
}

STATS_IGNORE_IPS = (
    '188.220.35.125',
    '127.0.0.1',
    '192.168.1.65',
    '192.168.1.64',
    '192.168.1.70',
    '192.168.1.67',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

AUTH_PROFILE_MODULE = 'users.UserProfile'
AUTHENTICATION_BACKENDS = (
    'apps.authenticate.backends.CustomUserBackend',
    'django.contrib.auth.backends.ModelBackend',
)
LOGIN_URL = '/authenticate/login.html'
LOGOUT_URL = '/authenticate/logout.html'
LOGIN_REDIRECT_URL  = '/'

COMPRESS = True
IMAGE_SIZES = ((1500,1058), (850,600), (612,450), (480,320), (320,240), (200,200) )

try:
    from settings_local import *
except ImportError:
    pass
