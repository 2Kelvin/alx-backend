#!/usr/bin/env python3
'''Get locale from request'''
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    '''class containing babel configurations'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    '''get the best language match'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''Renders 3-index.html template'''
    return render_template('3-index.html')
