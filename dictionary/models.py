from django.db import models

# Create your models here.
class Words(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    language = models.ForeignKey('Languages', on_delete=models.CASCADE)
    word = models.CharField(max_length=255)
    meaning= models.CharField(max_length=255)

class Languages(models.Model):
    name = models.CharField(max_length=100)
