from django.db import models

# Create your models here.

class aboutnew(models.Model):
    title = models.CharField(max_length=110,blank=False)

class picture(models.Model):
    topic = models.CharField(max_length=100,blank=False)    
    image = models.ImageField(upload_to='picture/',blank=False)

    
    