import unittest
from beerlistit.parse import *

class ParseTestCase(unittest.TestCase):
    """Tests for parse.py"""

    def test_fetch_page(self):
        """Does fetching a URL return the right document?"""
        html = fetch_page('http://google.com')
        self.assertIs(type(html), str)
        self.assertTrue('Google' in html)

    def test_fetch_page_fail(self):
        """Does fetching a nonexistant URL return None?"""
        html = fetch_page('http://google.com/jfnsdajnfnensensan')
        self.assertIsNone(html)

    def test_extract_beers(self):
        """Are beers successfully extracted from an HTML document?"""
        html = open('tests/example_menu_page.html', 'r').read()
        beers = extract_beers(html)
        self.assertIs(type(beers), list)
        self.assertEquals(len(beers), 14)
        self.assertIs(type(beers[0]), unicode)

    def test_extract_beers_fail(self):
        """Are fake beers unsuccessfully extracted from an HTML document?"""
        beers = extract_beers('<div>Fakebeer</div><span>Not a real beer</span>')
        self.assertIs(type(beers), list)
        self.assertEquals(len(beers), 0)
