# -*- coding: utf-8 -*-
from jamiecurle import config
from flask import render_template, redirect, request
from data import get_dates, get_posts, get_post, get_tags

def blog_redirect(**kwargs):
    url = '/blog.html'
    if kwargs.get('slug'):
        url = '/blog/%s/' % kwargs['slug']
    if kwargs.get('month') and kwargs.get('year'):
        url = '/blog/%s/%s/' % (kwargs['year'], kwargs['month'])
    return redirect(url, code=301)

def blog_tags():
    tags = get_tags()
    dates = get_dates()
    return render_template('blog/tags.html',tags=tags, dates=dates)

def blog_tagged(tag):
    tags = get_tags()
    dates = get_dates()
    tagged_posts = [post for post in get_posts() if tag in post['tags']]
    return render_template('blog/tagged.html', tagged_posts=tagged_posts,
        tag=tag, tags=tags, dates=dates)

def blog_post(slug):
    if slug.startswith('draft') and config.SHOW_DRAFTS == False:
        return render_template('404.html'), 404
    key = str('post_%s' % slug)
    post = get_post('%s.md' % slug )
    tags = get_tags()
    dates = get_dates()
    return render_template('blog/post.html', post=post, tags=tags,
        dates=dates)

def blog_archive(year, month):
    key = 'blog_archive_%s_%s' % (year, month)
    posts = get_posts()
    tags = get_tags()
    dates = get_dates()
    archive_posts = []
    for post in posts:
        if post['created'].month == month and post['created'].year == year:
            archive_posts.append(post)
    return render_template('blog/archive.html', posts=archive_posts, tags=tags,
        dates=dates)

def blog_index():
    posts = get_posts()[:20]
    tags = get_tags()
    dates = get_dates()
    return render_template( 'blog/index.html', posts=posts, tags=tags,
        dates=dates)
