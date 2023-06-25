from django.db import models


# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=40)
    comission = models.IntegerField()


class Student(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    email = models.EmailField()


class Proffesor(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    email = models.EmailField()
    profession = models.TextField(max_length=40)


class Exam(models.Model):
    name = models.CharField(max_length=40)
    time_delivery = models.DateField()
    delivered = models.BooleanField()
