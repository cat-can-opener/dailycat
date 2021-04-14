from django.db import models
from .cat import Cat
from django.urls import reverse

class Title(models.Model):

    """Title Model Definition"""

    cat = models.ForeignKey(Cat,on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('cat:detail', kwargs={'cat_id': self.cat.id})