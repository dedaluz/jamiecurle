# -*- coding: utf-8 -*-
DEBUG = False
CACHE_ENABLED = True
BLOG_CONTENT_PATH = '/your/path/here'
MEMCACHE_CONNECTION = 'unix:/home/curle/tmp/memcached.sock'
SHOW_DRAFTS = False

# override

try:
    from config_local import *
except ImportError:
    pass