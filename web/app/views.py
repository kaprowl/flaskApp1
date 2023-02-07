from flask import (jsonify, render_template,
                   request, url_for, flash, redirect)
import json
from sqlalchemy.sql import text
from app import app
from app import db


@app.route('/')
def home():
    return "Flask says 'Hello world!'"


@app.route('/crash')
def crash():
    return 1/0