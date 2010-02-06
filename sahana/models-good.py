from django.contrib.gis.db import models



class SahanaModel(models.Model):
    uuid = models.DateTimeField()
    modified_on = models.DateTimeField()
    created_on = models.DateTimeField()
   

class Hospital(SahanaModell):
    name = models.CharField(max_length=1024)
    address = models.CharField(max_length=1024,blank=True)
    city = models.CharField(max_length=1024,blank=True)
    phone_business = models.CharField(max_length=128,
    comments = models.CharField(max_length=1024,blank=True)
    location = models.PointField(srid=4326,null=True,blank=True)
    objects = models.GeoManager()
    

 
