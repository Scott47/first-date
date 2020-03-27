from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from .favorite import Favorite


class Customer(models.Model):

   user = models.OneToOneField(User, on_delete=models.CASCADE)
   favorite = models.ManyToManyField(Favorite, related_name="favorites")

   def __str__(self):
       return f'{self.first_name} {self.last_name}'

   class Meta:
       ordering = (F('user.date_joined').asc(nulls_last=True),)