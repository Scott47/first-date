from django.db import models
from .customer import Customer
from .comment import Comments

class Favorite (models.Model):

   place = models.CharField(max_length=200)
   zomato = models.CharField(max_length=10)