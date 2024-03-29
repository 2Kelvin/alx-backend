#!/usr/bin/env python3
'''Mock logging in'''
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


@app.before_request
def before_request():
    '''sets a user as a global'''
    g.user = get_user()


def get_user() -> Union[Dict, None]:
    '''returns a user dictionary'''
    loginId = request.args.get('login_as')
    if loginId and int(loginId) in users.keys():
        return users[int(loginId)]
    return None


@app.route('/')
def index() -> str:
    '''Renders 5-index.html template'''
    return render_template('5-index.html', user=g.user)
