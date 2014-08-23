import unittest
from beerlistit.annotate import *
from beerlistit.models import Beer

class AnnotateTestCase(unittest.TestCase):
    """Tests for annotate.py"""

    def test_update_urls(self):
        """Is the beer successfully annotated with a valid URL?"""
        beer = Beer(name=u'Highway to the danker zone')
        update_urls([beer])

        self.assertIs(type(beer), Beer)
        self.assertIs(type(beer.name), unicode)
        self.assertEquals(beer.name, u'Highway to the danker zone')
        self.assertIs(type(beer.url), unicode)
        self.assertEquals(beer.url, u'http://beeradvocate.com/beer/profile/32931/129037/')
        self.assertRaises(AttributeError, beer.rating)

    def test_update_urls_fail(self):
        """Is an unknown beer annotated with no URL?"""
        beer = Beer(name=u'thisbeerdoesnotexist')
        update_urls([beer])

        self.assertIs(type(beer), Beer)
        self.assertIs(type(beer.name), unicode)
        self.assertEquals(beer.name, u'thisbeerdoesnotexist')
        self.assertIs(type(beer.url), unicode)
        self.assertEquals(beer.url, u'')
        self.assertRaises(AttributeError, beer.rating)

    def test_update_ratings(self):
        """Is the beer successfully annotated with a valid rating?"""
        beer = Beer(name=u'Highway to the danker zone')
        update_urls([beer])
        update_ratings([beer])

        self.assertIs(type(beer), Beer)
        self.assertIs(type(beer.name), unicode)
        self.assertEquals(beer.name, u'Highway to the danker zone')
        self.assertIs(type(beer.url), unicode)
        self.assertEquals(beer.url, u'http://beeradvocate.com/beer/profile/32931/129037/')
        self.assertIs(type(beer.rating), int)
        self.assertTrue(beer.rating >= 0 and beer.rating <= 100)

    def test_update_ratings_fail(self):
        """Is an unknown beer annotated with no rating?"""
        beer1 = Beer(name=u'thisbeerdoesnotexist')
        beer2 = Beer(name=u'thisbeerdoesnotexisteither')
        update_urls([beer1])
        update_ratings([beer1, beer2])

        self.assertIs(type(beer1), Beer)
        self.assertIs(type(beer1.name), unicode)
        self.assertEquals(beer1.name, u'thisbeerdoesnotexist')
        self.assertIs(type(beer1.url), unicode)
        self.assertEquals(beer1.url, u'')
        self.assertRaises(AttributeError, beer1.rating)

        self.assertIs(type(beer2), Beer)
        self.assertIs(type(beer2.name), unicode)
        self.assertEquals(beer2.name, u'thisbeerdoesnotexisteither')
        self.assertIs(type(beer2.url), unicode)
        self.assertEquals(beer2.url, u'')
        self.assertRaises(AttributeError, beer2.rating)

    def test_extract_beer_url(self):
        """Is the correct beer profile URL found on a BA search results page?"""
        html = open('tests/example_result_page.html', 'r').read()
        url = extract_beer_url(html)
        self.assertIs(type(url), unicode)
        self.assertEquals(url, u'http://beeradvocate.com/beer/profile/32931/129037/')

    def test_extract_beer_url_fail(self):
        """Is None returned given an empty or invalid BA search results page?"""
        url = extract_beer_url('there is no URL here')
        self.assertIsNone(url)

    def test_extract_rating(self):
        """Is the correct rating extracted given a BA beer profile page?"""
        html = open('tests/example_beer_page.html', 'r').read()
        rating = extract_rating(html)
        self.assertIs(type(rating), int)
        self.assertEquals(rating, 93)

    def test_extract_rating_fail(self):
        """Is None returned given an invalid BA beer profile page?"""
        rating = extract_rating(u'no rating in here 94')
        self.assertIsNone(rating)
