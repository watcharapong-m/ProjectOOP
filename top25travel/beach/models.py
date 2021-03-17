from django.db import models

# Create your models here.
class top25travel(models.Model):
    names = models.CharField(max_length=50, blank=False)
    descriptions = models.TextField(blank=False)
    images = models.CharField(max_length=255,blank=False)