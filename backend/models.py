from django.db import models
from django.contrib.auth.models import User

class TopPost(models.Model):
    turi = models.CharField(max_length=255)

    def __str__(self):
        return self.turi

class Post(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    data = models.DateField(auto_now_add=False)
    many = models.ManyToManyField(TopPost, blank=True)
    down = models.FileField(upload_to='store/pdfs', max_length=255, null=True, default=None)
    down1 = models.ImageField(upload_to='store/covers')
    live = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    


    def __str__(self):
        return self.name



        
