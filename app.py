#! python3
"""random_fact_scraper.py - Scrape the http://randomfactgenerator.net website."""

import os
import json
import requests
from flask import Flask, Response
from lxml import html

app = Flask(__name__)

@app.route("/")
def index():
    return 'Ok!'

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

#-------------------------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
