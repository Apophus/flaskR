#!usr/bin/python

import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \ render_template, flash

#create the app
app = Flask(__name__)
app.config.from_object(__name__)

#load default config and override config from an environment variable
app.config.update(dict(
    DATABASE = os.paath.join(app.root_path, 'flaskr.db'),
    SECRET_KEY = 'development key',
    USERNAME ='admin',
    PASSWORD = 'default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent = True)

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
"""creates a db connection if there's none
yet for the app instance"""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
#closes db at the end ofthe request
    if hasattr(g, 'sqlite_db')
        gsqlite_db.close()


