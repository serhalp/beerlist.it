# vim: set fileencoding=utf-8 :

import operator
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

    # Count number of keyword-matching strings per unique tag-depth pair.
    locations = {}
    for s in soup.strings:
        if len(s) < LEN_THRESHOLD and frozenset(s.strip().lower().split()) & keywords:
            loc = (s.parent.name, node_depth(s))
            if loc in locations:
                locations[loc] += 1
            else:
                locations[loc] = 1

    if not locations:
        return []

    # Find tag-depth pair with maximal matches.
    maxloc = max(locations.iteritems(), key=operator.itemgetter(1))[0]

    # Get all strings matching this structure.
    parents = filter(lambda tag: node_depth(tag) == maxloc[1] - 1, soup.findAll(maxloc[0]))
    for p in parents:
        for s in p.findAll(text=True, recursive=False):
            s = s.strip()
            if s and len(s) < LEN_THRESHOLD:
                beers.append({ 'name': s })

    return beers

def node_depth(s):
    return sum(1 for _ in s.parents)
