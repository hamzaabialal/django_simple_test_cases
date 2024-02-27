from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

class StudentDetails(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    departement = models.CharField(max_length=300)
