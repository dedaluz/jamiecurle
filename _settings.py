# Django settings for jamiecurle project.
<<<<<<< HEAD
import os
ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

=======
from os import path
APP_ROOT = path.dirname(path.realpath(__file__))
APP_NAME = 'jamiecurle'

DISQUS_DEV = True
GRID = True
>>>>>>> 949b90c6a61412f3627470b45048cb441d979944
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
<<<<<<< HEAD
    # ('Your Name', 'your_email@domain.com'),
)

=======
    ('Jamie Curle', 'me@jamiecurle.com'),
)
INTERNAL_IPS = ('127.0.0.1')
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'django@designcc.co.uk'
EMAIL_HOST_PASSWORD = 'djangodjango'
EMAIL_PORT = 587
>>>>>>> 949b90c6a61412f3627470b45048cb441d979944
MANAGERS = ADMINS

DATABASES = {
    'default': {
<<<<<<< HEAD
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'jamiecurle2',                      # Or path to database file if using sqlite3.
        'USER': 'jcurle',                      # Not used with sqlite3.
=======
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'jamiecurle.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
>>>>>>> 949b90c6a61412f3627470b45048cb441d979944
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Europe/London'

<<<<<<< HEAD
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = path('media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://jamiecurle.jc/'

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
=======
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

MEDIA_ROOT = APP_ROOT + '/media'
MEDIA_URL = 'http://jamiecurle.d.jmcrl.com/'

ADMIN_MEDIA_PREFIX = '/media/'
SECRET_KEY = 'bo1-i*rt9+xv_1p(pl0@qxzyen$0+!5a2o1uy)-6e$7r%ot4ad'
>>>>>>> 949b90c6a61412f3627470b45048cb441d979944
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
<<<<<<< HEAD
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
=======
    'django.core.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'apps.utils.context_processors.grid'
>>>>>>> 949b90c6a61412f3627470b45048cb441d979944
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
<<<<<<< HEAD
    'johnny.middleware.LocalStoreClearMiddleware',
    'johnny.middleware.QueryCacheMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
=======
>>>>>>> 949b90c6a61412f3627470b45048cb441d979944
)

ROOT_URLCONF = 'jamiecurle.urls'

TEMPLATE_DIRS = (
<<<<<<< HEAD
    path('templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
=======
 '%s/templates/' % APP_ROOT, 
)

INSTALLED_APPS = (
>>>>>>> 949b90c6a61412f3627470b45048cb441d979944
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
<<<<<<< HEAD
    'django.contrib.markup',
    'south',
    'debug_toolbar',
    'johnny',
    'taggit',
    'compressor',
    'form_utils',
    'apps.posts',
)

JOHNNY_MIDDLEWARE_KEY_PREFIX='jamiecurle'
"""CACHES = {
        'default': {
            'BACKEND': 'johnny.backends.memcached.CacheClass',
            'LOCATION': '127.0.0.1:11211'
        }
}
"""
CACHE_BACKEND = 'johnny.backends.memcached://127.0.0.1:11211/'


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
IMAGE_SIZES = ((850,600), (200,200) )
=======
    'django.contrib.comments',
    'django.contrib.markup',
    'django.contrib.webdesign',
    'compressor',
    'tagging',
    'south',
    'disqus',
    'haystack',
    'debug_toolbar',
    'apps.blog',
    'apps.portfolio',
    'apps.books',
    'apps.assets',
    'apps.info',
    'apps.utils',
    'apps.ultra'
)
IMAGE_SIZES = ((2560,1440),(800,600),(290,240),(240,168),(140,96),(90,96))
# can remove this when blog assets are removed
PHOTO_SIZES = IMAGE_SIZES
COMPRESS=False
DISQUS_API_KEY = 'EfSTlwj9Em4u7gd4uTiNDXjBs6WYG4dLlavHflbgd1xA7sImLmCoCCg3VJj1wSuH'
DISQUS_WEBSITE_SHORTNAME = 'jamiecurle'
HAYSTACK_SITECONF = 'jamiecurle.search_sites'
HAYSTACK_SEARCH_ENGINE = 'xapian'
HAYSTACK_XAPIAN_PATH = '/Users/jcurle/Sites/jamiecurle/search_index'
HAYSTACK_INCLUDE_SPELLING = True


CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

#HAYSTACK_SEARCH_ENGINE = 'solr'
#HAYSTACK_SOLR_URL = 'http://127.0.0.1:8983/solr/'
#HAYSTACK_INCLUDE_SPELLING = True

#HAYSTACK_WHOOSH_PATH = '%s/index' % APP_ROOT

#HAYSTACK_SEARCH_ENGINE = 'whoosh'
#HAYSTACK_WHOOSH_PATH = '%s/index' % APP_ROOT
>>>>>>> 949b90c6a61412f3627470b45048cb441d979944
