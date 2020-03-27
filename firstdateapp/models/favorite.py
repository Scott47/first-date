from django.db import models

class Favorite (models.Model):

   place = models.CharField(max_length=200)
   zomato = models.CharField(max_length=10)