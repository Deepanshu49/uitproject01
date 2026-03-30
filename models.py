from django.db import models
class app1(models.Model):
    universityrollno=models.IntegerField(unique=True)
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.EmailField(max_length=255,unique=True)