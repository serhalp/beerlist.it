from django.http import HttpResponse

from server.models import Beer, BeerMenu
from beerlistit.beerlistit import list_it

def index(request):
    return HttpResponse('Hello, world.')

def all_beers(request):
    """Only useful for development."""
    beers = Beer.objects.all()
    return HttpResponse('Beers we know about:<br />' + _describe_beers(beers))

def beer(request, name):
    """Only useful for development."""
    beer = Beer.objects.get(name=name)
    return HttpResponse('Checking out beer %s' % beer)

def menu(request, url):
    menu = list_it(url)
    return HttpResponse('This menu contains these beers:<br />' + _describe_beers(menu.beers.order_by('-rating')))

def _describe_beers(beers):
    return '<br />'.join(['<a href="%s">%s</a>: <strong>%s</strong>' % (b.url or '#', b.name, b.rating or '?') for b in beers])
