 
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='posters/')
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title
