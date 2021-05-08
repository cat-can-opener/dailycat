from django.db import models
from django.urls import reverse

from .cat import Cat


class Title(models.Model):
    """Title Model Definition"""
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='title_set')
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)  # fk -> 1, 2, 3
    content = models.CharField(max_length=255)  # Char
    created = models.DateTimeField(auto_now_add=True)  # Datetime
    liked_counts = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('cat:detail', kwargs={'cat_id': self.cat.id})
