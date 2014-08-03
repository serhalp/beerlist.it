import re
import requests
import bs4

def fetch_page(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.content
    else:
        return None

def extract_beers(doc):
    """Given an HTML document, return a list of putative beers found therein."""
    beers = []
    soup = bs4.BeautifulSoup(doc)
    for s in soup.stripped_strings:
        if clean_beer_name(s) in known_beers:
            beers.append({ 'name': s })
    return beers

def clean_beer_name(beer_name):
    return re.sub('\W+', '', beer_name).lower()

known_beers = dict.fromkeys(map(clean_beer_name, open('beerlistit/beers.txt').readlines()))
