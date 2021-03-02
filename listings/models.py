from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=100,null=True)
    zipcode = models.CharField(max_length=20,null=True)
    description = models.TextField(blank=True,null=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1,null=True)
    garage = models.IntegerField(default=0,null=True)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1,null=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/',null=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,null=True)
    
    is_published = models.BooleanField(default=True,null=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True,null=True)
    def __str__(self):
        return self.title
    