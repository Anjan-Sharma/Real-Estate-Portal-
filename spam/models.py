from django.db import models
from django.contrib.auth.models import User
from listings.models import Listing
from datetime import datetime
from django.utils import timezone

# Create your models here.



class Spam_filtering(models.Model):
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    comments = models.TextField(blank=True,max_length=1000)
    type = models.CharField(blank=True,max_length=100)
    timestamp = models.DateTimeField(default=datetime.now(),null=True)

    def __str__(self):
        return '{}  - Predicted as:  {}'.format(self.comments,str(self.type),self.type)
        # return self.type