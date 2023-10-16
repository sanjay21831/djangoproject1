from django.db import models

# Create your models here.
class StudentsData(models.Model):
    fist_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=40)
    course = models.CharField(max_length=50)
    fee = models.IntegerField()
    assigment1 = models.IntegerField()
    assigment2 = models.IntegerField()
    assigment3 = models.IntegerField()
    assigment4 = models.IntegerField()
    institute = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    