from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from cats.models import Cat, Title


class User(AbstractUser):
    '''
    User 모델

    '''
    liked_cats = models.ManyToManyField(Cat, related_name='user_set')
    liked_titles = models.ManyToManyField(Title, related_name='user_set')

    def __str__(self):
        return self.username
