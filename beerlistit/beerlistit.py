from parse import fetch_page, extract_beers
from annotate import annotate

def list_it(url):
    doc = fetch_page(url)
    beers = extract_beers(doc)
    for beer in beers:
        annotate(beer)
    return beers
