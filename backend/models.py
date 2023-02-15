from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=255)
    soni = models.IntegerField(default=1)
    img = models.CharField(max_length=255)
    down = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name
