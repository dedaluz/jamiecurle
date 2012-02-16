# -*- coding: utf-8 -*-
DEBUG = False
CACHE_ENABLED = True
BLOG_CONTENT_PATH = '/your/path/here'
MEMCACHE_CONNECTION = '127.0.0.1:11211'
SHOW_DRAFTS = False

# override

try:
    from config_local import *
except ImportError:
    pass