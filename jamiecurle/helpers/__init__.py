# -*- coding: utf-8 -*-
from lazyload import LazyLoad
from cache import get_cached, set_cached

def url(app, url_rule, import_name, **options):
    view = LazyLoad('jamiecurle.' + import_name)
    app.add_url_rule(url_rule, view_func=view, **options)


def filter(app, filter_name, import_name):
    filter_func = LazyLoad('jamiecurle.' + import_name)
    app.jinja_env.filters[filter_name]=filter_func    