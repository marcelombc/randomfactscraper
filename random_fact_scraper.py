#! python3
"""random_fact_scraper.py - Scrape the http://randomfactgenerator.net website."""

from lxml import html
import requests


def main():
    page = requests.get('http://randomfactgenerator.net')
    tree = html.fromstring(page.content)
    facts = tree.xpath('//div[@id="z"]/text()')

    print(list(filter(lambda x: x!= '\n\n', facts)))


#-------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
