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
