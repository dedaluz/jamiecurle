# -*- coding: utf-8 -*-
from flask import render_template

def project_index():
    return render_template('projects/index.html')