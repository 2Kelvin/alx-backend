#!/usr/bin/env python3
'''Use user locale'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from typing import Union, Dict
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError
import datetime


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


@app.before_request
def before_request():
    '''sets a user as a global'''
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    '''get the best language match'''
    lang = request.args.get('locale')
    if lang and lang in app.config['LANGUAGES']:
        return lang
    elif g.user and g.user["locale"] in app.config['LANGUAGES']:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[Dict, None]:
    '''returns a user dictionary'''
    loginId = request.args.get('login_as')
    if loginId and int(loginId) in users.keys():
        return users[int(loginId)]
    return None


@babel.timezoneselector
def get_timezone() -> str:
    '''use the timezone from user dictionary'''
    urlTimezone = request.args.get('timezone')
    if urlTimezone:
        try:
            return timezone(urlTimezone)
        except UnknownTimeZoneError:
            pass
    elif g.user and g.user["timezone"]:
        try:
            return timezone(g.user["timezone"])
        except UnknownTimeZoneError:
            pass
    return timezone('UTC')


@app.route('/')
def index() -> str:
    '''Renders index.html template'''
    currentTime = format_datetime(datetime.datetime.now())
    return render_template('index.html', user=g.user, currentTime=currentTime)
