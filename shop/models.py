from distutils.command.upload import upload
from django.db import models

class user(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phoneno = models.IntegerField()

class profile(models.Model):
    user = models.OneToOneField(user,on_delete=models.CASCADE)
    profilephoto = models.ImageField(upload_to='media')
