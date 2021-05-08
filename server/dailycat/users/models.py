from django.db import models
from django.contrib.auth.models import AbstractUser
from cats.models import Cat, Title


class User(AbstractUser):
    '''
    User 모델

    '''
    # first_name = None
    # last_name = None
    # username = None
    # email = models.EmailField(unique=True)
    # password = models.CharField(max_length=128)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    liked_cats = models.ManyToManyField(Cat, related_name='user_set')
    liked_titles = models.ManyToManyField(Title, related_name='user_set')

    def __str__(self):
        return self.username
