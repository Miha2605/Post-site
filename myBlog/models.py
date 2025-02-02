from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default="sport")
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.author} {self.text}'
    def get_absolute_url(self):
        return reverse('article_detail',args=(str(self.pk)))

class Category(models.Model):
    name = models.CharField(max_length = 255)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("home")

















