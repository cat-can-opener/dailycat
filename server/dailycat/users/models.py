from django.db import models
from django.core.validators import EmailValidator
from cats.models import Cat, Title


class User(models.Model):
    '''
    User 모델
    - password는 사용하지 않음
    - email만으로 간단하게 세션 유지
    '''
    email = models.EmailField(unique=True, validators=[
                              EmailValidator])  # EmailValidator
    created = models.DateTimeField(auto_now_add=True)
    liked_cats = models.ManyToManyField(Cat)
    liked_titles = models.ManyToManyField(Title)
