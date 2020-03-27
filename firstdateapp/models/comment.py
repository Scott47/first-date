from django.db import models


class Comment(models.Model):

   comment = models.Charfield(max_length=2500)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   class Meta:
       ordering = ("createdtime")
       verbose_name = ("comment")
       verbose_name_plural = ("comments")

   def __str__(self):
       return f' {self.user.name} at {self.createdtime}'