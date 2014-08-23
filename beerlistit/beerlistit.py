from parse import fetch_page, extract_beers
from annotate import annotate

from models import Beer, BeerMenu

def list_it(url):
    if BeerMenu.objects.filter(url=url).exists():
        return BeerMenu.objects.get(url=url)
    menu = BeerMenu.objects.create(url=url)

    doc = fetch_page(url)
    beer_names = extract_beers(doc)
    for name in beer_names:
        beer = Beer.objects.get_or_create(name=name)[0]
        annotate(beer)
        menu.beers.add(beer)

    menu.save()

    return menu
