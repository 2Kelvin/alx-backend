#!/usr/bin/env python3
'''Basic flask app'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index() -> str:
    '''Renders 0-index.html template'''
    return render_template('0-index.html')
