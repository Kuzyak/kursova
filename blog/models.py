from django.db import models
from PIL import Image

class Teg(models.Model):
    name = models.CharField(max_length=200)
    def dodaty(self):
        self.save()
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    images = models.ImageField(upload_to='static/images', blank=True)
    teg = models.ManyToManyField(Teg)

    def publish(self):
        self.save()
    def __str__(self):
        return self.title
