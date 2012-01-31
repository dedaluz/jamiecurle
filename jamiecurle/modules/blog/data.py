# -*- coding: utf-8 -*-
import yaml
import os
import markdown
import codecs
from collections import OrderedDict, Counter
from operator import itemgetter
from jamiecurle.helpers import get_cached, set_cached
from jamiecurle.config import BLOG_CONTENT_PATH



def get_post(slug):
    key = str('get_post_%s' % slug.replace('.md', ''))
    cache = get_cached(key)
    if cache:
        return cache
    item = '%s%s' % (BLOG_CONTENT_PATH, slug)
    with codecs.open(item, encoding='UTF-8') as md_file:
        contents = md_file.read()
    # split into yaml and markdown
    parts = contents.split('---')
    header = yaml.load(parts[0])
    content = markdown.markdown(parts[1])
    try:
        tags = header['tags']
    except KeyError:
        tags = []
    # now append a dict wit the info to posts
    post = {
        'url': '/blog/%s/' % item.split('/').pop().split('.')[0],
        'title': header['title'],
        'description': header['description'],
        'created': header['created'],
        'tags': tags,
        'content': content
    }
    set_cached(key, post)
    return post


def get_md_files():
    cache = get_cached('get_md_files')
    if cache:
        return cache
    ls = [] # list of all markdown files
    for thing in os.listdir(BLOG_CONTENT_PATH):
        try:
            ext = thing.split('.').pop()
            if ext == 'md':
                ls.append(thing)
        except IndexError:
            pass
    set_cached('get_md_files', ls)
    return ls

def get_posts():
    cache = get_cached('get_posts')
    if cache:
        return cache
    #
    md_files = get_md_files()
    posts = [] # list of posts
    # now render out the posts from the list
    posts = []
    for md in md_files:
        post = get_post(md)
        posts.append(post)
    # sort them by date
    sorted_posts = sorted(posts, key=itemgetter('created'), reverse=True)
    set_cached('get_posts', sorted_posts)
    return sorted_posts

def get_tags():
    cache = get_cached('get_tags')
    if cache:
        return cache
    posts = get_posts()
    tag_list = []
    for post in posts:
        for tag in post['tags']:
            tag_list.append(tag)
    tags = Counter(tag_list).most_common()
    set_cached('get_tags', tags)
    return tags

def get_dates():
    cache = get_cached('get_dates')
    if cache:
        return cache
    posts = get_posts()
    dates = OrderedDict()
    for post in posts:
        key = post['created'].strftime('%Y_%m')
        try:
            dates[key][1] = dates[key][1] + 1
        except KeyError:
            dates[key] = [post['created'], 1]
    set_cached('get_dates', dates)
    return dates