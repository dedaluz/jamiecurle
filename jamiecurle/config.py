# -*- coding: utf-8 -*-
DEBUG = True
CACHE_ENABLED = True
BLOG_CONTENT_PATH = '/your/path/here'
MEMCACHE_CONNECTION = '127.0.0.1:11211'

# override

try:
    from config_local import *
except ImportError:
    pass