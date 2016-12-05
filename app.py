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
    page = requests.get("http://randomfactgenerator.net")
    tree = html.fromstring(page.content)
    facts = list(filter(lambda x: x!= "\n\n",
                 tree.xpath("//div[@id='z']/text()")))
    data = json.dumps({ "text": facts[0] })
    resp = Response(response=data,
        status=200, \
        mimetype="application/json")

    return resp

#-------------------------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
