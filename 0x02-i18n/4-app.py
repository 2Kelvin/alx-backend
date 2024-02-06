#!/usr/bin/env python3
'''Force locale with URL parameter'''
from flask import Flask, render_template, request
from flask_babel import Babel


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
    lang = request.args.get('locale')
    if lang and lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''Renders 4-index.html template'''
    return render_template('4-index.html')
