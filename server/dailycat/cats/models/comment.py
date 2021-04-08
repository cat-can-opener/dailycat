from django.db import models
from .title import Title 

class Comment(models.Model):

   """ Comment Model Definition """

   title = models.ForeignKey(Title,on_delete=models.CASCADE)
   content = models.CharField(max_length=255)
   created = models.DateTimeField(auto_now_add=True)