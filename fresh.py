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

@app.route('/')
def index():
  return render_template('index.tpl')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    dbg = True
    app.run(debug=dbg)
