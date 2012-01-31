import os, re, sys
from flask import Flask



def create_app(name = __name__):
    app = Flask(__name__, static_path='/static')
    app.config.from_pyfile('config.py')
    #load_config(app)
    #register_local_modules(app)
    return app

