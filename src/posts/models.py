from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from django.urls import reverse


class Post(models.Model):
    title=models.CharField(max_length=100)
    subtext=models.CharField(max_length=250)
    thumbnail = models.ImageField(default='')
    content=RichTextField(blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
        }) 
class Photo(models.Model):
    subtext=models.CharField(max_length=100)
    image = models.ImageField(default='')
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subtext