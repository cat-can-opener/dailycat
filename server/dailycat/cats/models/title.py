from django.db import models
from .cat import Cat

class Title(models.Model):

    """Title Model Definition"""

    cat = models.ForeignKey(Cat,on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)