#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, url_for, request, render_template, redirect, flash, g
from database import db_session, init_db
from pdb import set_trace as debugger
import os

# create flask app
app = Flask(__name__)

# some flask configurations
app.config.from_object('config.DevelopmentConfig')

@app.route('/')
def index():
  return render_template('index.tpl')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.tpl'), 404

@app.after_request
def shutdown_session(response):
    db_session.remove()
    return response

if __name__ == '__main__':
    dbg = True
    app.run(debug=dbg)
