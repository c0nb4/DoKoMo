from django.db import models

import imp
from django.db import models
from datetime import datetime

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length = 200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    doko_name  = models.CharField(max_length= 200)
    description = models.TextField(blank=True)
    cash_payed = models.IntegerField()
    games_played = models.IntegerField()
   
    def __str__(self) -> str:
        return self.name 
          
