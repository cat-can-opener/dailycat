from django.db import models


class Cat(models.Model):

    """ Cat Model Definition """
    
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    expose_date = models.DateField(null=True)
    is_reported = models.IntegerField(default=0)