from django.db import models

# Create your models here.

class offers(models.Model):
    title = models.CharField (max_length=100,blank=False)
    description = models.CharField(max_length=100,blank=False)

class picture(models.Model):
    image = models.ImageField(upload_to= 'picture/',blank = False)

class picture(models.Model):
    image = models.ImageField(upload_to= 'picture/',blank = False)

class client(models.Model):
    name = models.CharField (max_length=100,blank=False)
    link = models.CharField (max_length=100,blank=False)
    image = models.ImageField(upload_to= 'client/',blank = False)

class contactform(models.Model):
    name = models.CharField (max_length=100,blank=False)
    email = models.CharField (max_length=100,blank=False)
    subject = models.CharField (max_length=100,blank=False)
    message = models.TextField (max_length=100,blank=False)

       



