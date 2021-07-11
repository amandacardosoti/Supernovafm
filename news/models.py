from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    # www.supernova.com/blog/noticias
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_image/', blank=True)
    carrossel = models.BooleanField(default=False)
    
    