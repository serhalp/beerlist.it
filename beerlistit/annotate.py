import grequests
import bs4

from models import Beer

def update_urls(beers):
    rs = []
    for beer in beers:
        if not beer.url:
            def update_url(r, beer=beer, **kwargs):
                url = extract_beer_url(r.content)
                if url:
                    beer.url = url
            rs.append(grequests.get('http://beeradvocate.com/search/', \
                                    params={'qt': 'beer', 'q': beer.name}, \
                                    hooks={'response': update_url}))
    grequests.map(rs)

def update_ratings(beers):
    rs = []
    for beer in beers:
        if beer.url:
            def update_rating(r, beer=beer, **kwargs):
                beer.rating = extract_rating(r.content)
            rs.append(grequests.get(beer.url, hooks={'response': update_rating}))
    grequests.map(rs)

def extract_beer_url(html):
    try:
        return 'http://beeradvocate.com' + unicode(bs4.BeautifulSoup(html).find(id='baContent').find('a')['href'])
    except:
        return None

def extract_rating(html):
    try:
        return int(bs4.BeautifulSoup(html).find('span', attrs={'class': 'BAscore_big'}).string)
    except:
        return None
