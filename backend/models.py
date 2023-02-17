from django.db import models



class Nomi(models.Model):
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi 
 
class Post(models.Model):
    name = models.ManyToManyField(Nomi,blank=True)
    soni = models.IntegerField(default=1)
    img = models.CharField(max_length=255)
    down = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return f' {self.soni} - vazifa '





class Certificate(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    cert = models.FileField(upload_to='cert/', blank=True, null=True)


    def download_link(self):
        self.cert.url

        
