# -*- coding: utf-8 -*-
from flask import render_template

def home():
    return render_template('home.html')

def about():
    return render_template('about.html')