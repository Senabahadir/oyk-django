from django.db import models


class Post(models.Model):
    yayinla = models.BooleanField(default=False)
    baslik= models.CharField(max_length=200, unique = True)
    link = models.SlugField(max_length=200, unique=True)  #SlugField = link
    resim = models.ImageField(upload_to='blog_resim/')
    icerik = models.TextField()
    olusturma = models.DateTimeField(auto_now_add=True)
    guncelleme = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Baslik : " + self.baslik

# a= None  -> null
# a=''     -> blank