# vim: set fileencoding=utf-8 :

import re
import requests
import bs4

keywords = frozenset([
    u'stout', u'porter', u'saison', u'farmhouse', u'ale', u'lager', u'ipa', u'eisbock',
    u'pale', u'dark', u'double', u'imperial', u'amber', u'wheat', u'brown', u'red', u'barleywine',
    u'black', u'strong', u'cream', u'belgian', u'dubbel', u'tripel', u'quadrupel', u'quad',
    u'lambic', u'bitter', u'esb', u'altbier', u'weissbier', u'dunkel', u'dunkelweizen', u'kolsh',
    u'kölsch', u'weizenbock', u'bock', u'irish', u'gruit', u'wee', u'pilsner', u'pilsener',
    u'steam', u'witbier', u'kellerbier', u'dunkel', u'helles', u'rauchbier', u'vienna'
])
LEN_THRESHOLD = 30

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
        if len(s) < LEN_THRESHOLD and frozenset(s.lower().split()) & keywords:
            beers.append({ 'name': s })
    return beers
