import requests
import bs4

def annotate(beer):
    beer['url'] = url = find_beer_page(beer['name'])
    if url:
        beer['rating'] = find_beer_rating(url)

def find_beer_page(beer_name):
    html = requests.get('http://beeradvocate.com/search/', params={'qt': 'beer', 'q': beer_name}).content
    url = extract_beer_url(html)
    return 'http://beeradvocate.com' + url if url else None

def extract_beer_url(html):
    try:
        return str(bs4.BeautifulSoup(html).find(id='baContent').find('a')['href'])
    except:
        return None

def find_beer_rating(beer_url):
    return extract_rating(requests.get(beer_url).content)

def extract_rating(html):
    try:
        return int(bs4.BeautifulSoup(html).find('span', attrs={'class': 'BAscore_big'}).string)
    except:
        return None