#! python3
"""random_fact_scraper.py - Scrape the http://randomfactgenerator.net website."""

import os
import requests
from flask import Flask
from lxml import html

app = Flask(__name__)

@app.route("/")
def main():
    page = requests.get("http://randomfactgenerator.net")
    tree = html.fromstring(page.content)
    facts = tree.xpath("//div[@id='z']/text()")

    return list(filter(lambda x: x!= "\n\n", facts))


#-------------------------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
