from django.db import models


# Create your models here.
class patients(models.Model):
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=60)
    clothe = models.CharField(max_length=40)
    date = models.DateField(max_length=10)
    gender = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    document = models.FileField(upload_to ='uploads/')
    photo = models.FileField(upload_to="images/")

