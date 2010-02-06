from django.contrib.gis.db import models

class Category(models.Model):
    ushahidi_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    color = models.CharField(max_length=8, null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    objects = models.GeoManager()
    def __unicode__(self):
        return self.title
    class Meta:
	verbose_name_plural = "Categories"


class Country(models.Model):
    ushahidi_id = models.IntegerField()
    iso = models.CharField(max_length=2)
    name = models.CharField(max_length=255)
    capital = models.CharField(max_length=255)
    objects = models.GeoManager()
    def __unicode__(self):
        return self.name
    class Meta:
	verbose_name_plural = "Countries"

	
class Location(models.Model):
    ushahidi_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    country = models.ForeignKey(Country, null=True, blank=True)
    point = models.PointField()
    objects = models.GeoManager()
    def __unicode__(self):
        return self.name

class Media(models.Model):
    ushahidi_id = models.IntegerField()
    title = models.CharField(max_length=255)
    media_type = models.IntegerField(blank=True, null=True)
    media_link = models.CharField(max_length=1500, null=True, blank=True)
    media_thumb = models.CharField(max_length=1500, null=True, blank=True)

class Incident(models.Model):
    ushahidi_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateTimeField(null=True, blank=True)
    mode = models.IntegerField()
    active = models.BooleanField()
    verified = models.BooleanField()	
    location = models.ForeignKey(Location, blank=True, null=True)
    categories = models.ManyToManyField(Category)	
    media = models.ManyToManyField(Media,blank=True)
    objects = models.GeoManager()
    def __unicode__(self):
        return self.title
