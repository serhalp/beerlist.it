import unittest
from beerlistit.annotate import *

class AnnotateTestCase(unittest.TestCase):
    """Tests for annotate.py"""

    def test_annotate(self):
        """Is the beer successfully annotated with a valid URL and rating?"""
        beer = { 'name': 'Highway to the danker zone' }
        annotate(beer)

        self.assertTrue('url' in beer)
        self.assertIs(type(beer['url']), str)
        self.assertEquals(beer['url'], 'http://beeradvocate.com/beer/profile/32931/129037/')
        self.assertTrue('rating' in beer)
        self.assertIs(type(beer['rating']), int)
        self.assertTrue(beer['rating'] >= 0 and beer['rating'] <= 100)

    def test_annotate_fail(self):
        """Is an unknown beer annotated with a None URL and no rating?"""
        beer = { 'name': 'thisbeerdoesnotexist' }
        annotate(beer)

        self.assertTrue('url' in beer)
        self.assertIsNone(beer['url'])
        self.assertFalse('rating' in beer)

    def test_find_beer_page(self):
        """Is a BA beer profile URL given a valid beer name?"""
        url = find_beer_page('Highway to the danker zone')
        self.assertIs(type(url), str)
        self.assertEquals(url, 'http://beeradvocate.com/beer/profile/32931/129037/')

    def test_find_beer_page_fail(self):
        """Is None returned given an invalid beer name?"""
        url = find_beer_page('fdsnffefnadsjnfdksjfnaejw')
        self.assertIsNone(url)

    def test_extract_beer_url(self):
        """Is the correct beer profile URL found on a BA search results page?"""
        html = open('tests/example_result_page.html', 'r').read()
        url = extract_beer_url(html)
        self.assertIs(type(url), str)
        self.assertEquals(url, '/beer/profile/32931/129037/')

    def test_extract_beer_url_fail(self):
        """Is None returned given an empty or invalid BA search results page?"""
        url = extract_beer_url('there is no URL here')
        self.assertIsNone(url)

    def test_find_beer_rating(self):
        """Is a rating successfully found given a BA beer profile page?"""
        rating = find_beer_rating('http://beeradvocate.com/beer/profile/32931/129037/')
        self.assertIs(type(rating), int)
        self.assertTrue(rating >= 0 and rating <= 100)

    def test_find_beer_rating_fail(self):
        """Is None returned given an invalid BA beer profile page?"""
        rating = find_beer_rating('http://beeradvocate.com/beer/profile/99999/999999/')
        self.assertIsNone(rating)

    def test_extract_rating(self):
        """Is the correct rating extracted given a BA beer profile page?"""
        html = open('tests/example_beer_page.html', 'r').read()
        rating = extract_rating(html)
        self.assertIs(type(rating), int)
        self.assertEquals(rating, 93)

    def test_extract_rating_fail(self):
        """Is None returned given an invalid BA beer profile page?"""
        rating = extract_rating('no rating in here 94')
        self.assertIsNone(rating)
