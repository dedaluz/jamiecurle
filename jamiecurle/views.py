# -*- coding: utf-8 -*-
from flask import render_template, make_response
from jamiecurle import create_app
from jamiecurle.modules.blog.views import blog_index


app = create_app()

@app.errorhandler(404)
def page_not_found(error, *args):
    return render_template('404.html')

def home():
    return blog_index()

def about():
    return render_template('about.html')
