# -*- coding: utf-8 -*-
from flask import render_template, make_response
from jamiecurle import create_app
from jamiecurle.modules.blog.data import get_posts


app = create_app()

@app.errorhandler(404)
def page_not_found(error, *args):
    return render_template('404.html')

def home():
    post = get_posts()[0]
    return render_template('home.html', post=post)

def about():
    return render_template('about.html')
