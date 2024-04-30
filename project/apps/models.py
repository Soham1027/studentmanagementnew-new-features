from django.db import models
from django.contrib.auth.models import User,AbstractUser
from datetime import datetime,date

# Create your models here.
    
class STAaccounts(AbstractUser):
    USER=(
        ('1','Admin'),
        ('2','Staff'),
        ('3','Student'),
    )
    p_type=models.CharField(choices=USER,max_length=50,default=1) # type: ignore

class Subject(models.Model):
    name=models.CharField(max_length=25,null=True)
    class_name=models.CharField(max_length=25,null=True)
    
    
class Student(models.Model):
    admin=models.OneToOneField(STAaccounts, on_delete=models.CASCADE)
    gender=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.admin.username

class Staff(models.Model):
    admin = models.OneToOneField(STAaccounts,on_delete=models.CASCADE)
    email=models.CharField(max_length=100)
    gender =models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.admin.username


class timetable(models.Model):
    
    name=models.CharField(max_length=100)
    
    class_name=models.IntegerField()
    section_name =models.CharField(max_length=100)
    
    subject=models.CharField(max_length=100)
    start_time=models.IntegerField()
    end_time= models.IntegerField()
    


    def __str__(self):
        return self.name

    
   
    