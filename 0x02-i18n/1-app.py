#!/usr/bin/env python3
'''Basic babel setup'''
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    '''class containing languages prop'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index() -> str:
    '''Renders 1-index.html template'''
    return render_template('1-index.html')