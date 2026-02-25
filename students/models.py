from django.db import models

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    address = models.TextField()
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name