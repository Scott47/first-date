from django.db import models


class Comment(models.Model):

   comment = models.CharField(max_length=250)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   class Meta:
       verbose_name = ("comment")
       verbose_name_plural = ("comments")

   def __str__(self):
       return f' {self.user.name} at {self.createdtime}'