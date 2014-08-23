from django.db import models

class Beer(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(blank=True, null=True, default='')
    rating = models.SmallIntegerField(blank=True, null=True, default=None)

    def __unicode__(self):
        return self.name

class BeerMenu(models.Model):
    url = models.URLField()
    beers = models.ManyToManyField(Beer)

    def __unicode__(self):
        return self.url
