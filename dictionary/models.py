from django.db import models

# Create your models here.

class Languages(models.Model):  
    name = models.CharField(max_length=100)

class Words(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    word = models.CharField(max_length=1000)
    meaning= models.CharField(max_length=1000)
    language = models.ForeignKey('Languages', on_delete=models.CASCADE)