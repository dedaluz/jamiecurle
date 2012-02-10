# -*- coding: utf-8 -*-
from flask import render_template
from jamiecurle.modules.blog.data import get_posts

def home():
    post = get_posts()[0]
    return render_template('home.html', post=post)

def about():
    return render_template('about.html')
