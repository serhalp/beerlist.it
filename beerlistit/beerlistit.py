from parse import fetch_page, extract_beers
from annotate import update_urls, update_ratings

from models import Beer, BeerMenu

def list_it(url):
    if BeerMenu.objects.filter(url=url).exists():
        return BeerMenu.objects.get(url=url)
    menu = BeerMenu.objects.create(url=url)

    doc = fetch_page(url)
    beer_names = extract_beers(doc)
    beers = [Beer.objects.get_or_create(name=name)[0] for name in beer_names]
    menu.beers.add(*beers)
    update_urls(beers)
    update_ratings(beers)

    for beer in beers:
        beer.save()
    menu.save()

    return menu
