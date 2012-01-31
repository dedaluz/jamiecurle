import os
import yaml
import re
import markdown
import pygments
import calendar
import codecs
import memcache
from collections import OrderedDict, Counter
from operator import itemgetter
from pygments import lexers, formatters
from BeautifulSoup import BeautifulSoup
from flask import Flask, render_template
from flaskext.markdown import Markdown



Markdown(app)
MC = memcache.Client(['127.0.0.1:11211'], debug=0)
CACHE_ENABLED = True
#
#
# attempt overrides
try:
    from settings_local import *
except ImportError:
    pass






#
#
# views

