from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)
    post = models.CharField(max_length=100)

    class Meta:
        db_table = "Employee"
        
    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    fee = models.IntegerField()
    duration = models.IntegerField()
    class Meta:
        db_table = "Course"
    def __str__(self):
        return self.name
    
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    class Meta:
        db_table = 'Department'
    def __str__(self):
        return self.name
