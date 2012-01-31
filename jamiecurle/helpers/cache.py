# -*- coding: utf-8 -*-
import memcache
from jamiecurle.config import CACHE_ENABLED, MEMCACHE_CONNECTION

MC = memcache.Client([MEMCACHE_CONNECTION], debug=0)

def set_cached(key, value):
    MC.set(key, value, 0)

def get_cached(key):
    if not CACHE_ENABLED:
        return None
    return MC.get(key)