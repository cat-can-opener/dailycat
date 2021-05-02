from django.db import models
from .cat import Cat
from django.urls import reverse


class Title(models.Model):
    """Title Model Definition"""
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)  # fk -> 1, 2, 3
    content = models.CharField(max_length=255)  # Char
    created = models.DateTimeField(auto_now_add=True)  # Datetime

    def get_absolute_url(self):
        return reverse('cat:detail', kwargs={'cat_id': self.cat.id})
