from email.policy import default
from django.db import models

# Create your models here.

class Article(models.Model):
    Title = models.CharField(max_length=255)
    Description = models.CharField(max_length=3000)
    image = models.CharField(max_length=3000)
    Link = models.CharField(max_length=2500)

