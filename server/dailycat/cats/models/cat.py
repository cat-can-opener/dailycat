from django.db import models
from django.urls import reverse

class Cat(models.Model):

    """ Cat Model Definition """
    
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    expose_date = models.DateField(null=True)
    reported_counts = models.IntegerField(default=0)
    is_reported = models.BooleanField(default=False)
    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('cat:detail', kwargs={'pk': self.pk})
 