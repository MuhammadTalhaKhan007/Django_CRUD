from django.db import models

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    grade = models.CharField(max_length=2)
    address = models.TextField()
    contactNumber = models.CharField(max_length=15)

    def __str__(self):
        return self.firstName + " " + self.lastName
