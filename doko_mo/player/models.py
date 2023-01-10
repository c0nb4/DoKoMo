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
          

class Card(models.Model):
    SUIT_CHOICES = (
        ('heart', '♥'),
        ('diamond', '♦'),
        ('spade', '♠'),
        ('club', '♣'),
    )

    RANK_CHOICES = (
        ('ace', 'A'),
        ('king', 'K'),
        ('queen', 'Q'),
        ('jack', 'J'),
        ('ten', '10'),
        ('nine', '9'),
    )
   
    suit = models.CharField(max_length=7, choices=SUIT_CHOICES)
    rank = models.CharField(max_length=4, choices=RANK_CHOICES)

    def __str__(self):
        return self.get_suit_display() + self.get_rank_display()
