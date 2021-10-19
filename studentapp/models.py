from django.db import models

class Students(models.Model):
    StudentId = models.IntegerField()
    StudentGrade = models.IntegerField()
# Create your models here.
