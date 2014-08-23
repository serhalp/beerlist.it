from setuptools import setup

setup(name='beerlistit',
      version='0.1',
      description='Quickly get the BeerAdvocate ratings for all the beers listed on a page.',
      url='http://github.com/serhalp/beerlist.it',
      author='Philippe Serhal and Curtis Heberle',
      author_email='philippe.serhal@gmail.com',
      license='GPLv2',
      packages=['beerlistit'],
      install_requires=[
          'BeautifulSoup4',
          'grequests'
          'django'
      ],
      zip_safe=True)

