# -*- coding: utf-8 -*-
"""
dependencies:
  >>> easy_install Flask
  >>> easy_install Flask-WTF
  >>> easy_install simplejson
  >>> easy_install Flask-Babel
  >>> easy_install Flask-Mail
"""
from flask import Flask, url_for, request, render_template, redirect, flash
from pdb import set_trace as debugger
import os

# create flask app
app = Flask(__name__)

# some flask configurations
app.config.update(
    SECRET_KEY = '2b020728f54c912f4635135459b17d8a54e2dabc',
    MAIL_SERVER = 'smtp.webfaction.com',
    MAIL_PORT = 25,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = False,
    MAIL_DEBUG = app.debug,
    DEFAULT_MAIL_SENDER = None,
    MAIL_USERNAME = 'someuser',
    MAIL_PASSWORD = 'secret'
)

@app.route('/')
def index():
  return render_template('index.tpl')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.tpl'), 404

if __name__ == '__main__':
    dbg = True
    app.run(debug=dbg)
