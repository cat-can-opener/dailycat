from django.db import models
from django.contrib.auth.models import AbstractUser
from cats.models import Cat, Title


class User(AbstractUser):
    '''
    User 모델

    '''

    liked_cats = models.ManyToManyField(Cat)
    liked_titles = models.ManyToManyField(Title)

    def __str__(self):
        return self.username
