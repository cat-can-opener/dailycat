from django.db import models
from django.contrib.auth import get_user_model

from .title import Title

User = get_user_model()


class Comment(models.Model):
    """ Comment Model Definition """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment_set')
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
