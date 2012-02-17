# -*- coding: utf-8 -*-
DEBUG = False
MANIFEST_ENABLED = True
CACHE_ENABLED = True
BLOG_CONTENT_PATH = '/home/curle/sites/jamiecurle/jamiecurle/jamiecurle/content/blog'
MEMCACHE_CONNECTION = 'unix:/home/curle/tmp/memcached.sock'
SHOW_DRAFTS = False

# override

try:
    from config_local import *
except ImportError:
    pass