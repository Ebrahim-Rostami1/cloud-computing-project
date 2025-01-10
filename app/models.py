from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    is_watch = models.BooleanField(default=False)

    def __str__(self):
        return self.title
