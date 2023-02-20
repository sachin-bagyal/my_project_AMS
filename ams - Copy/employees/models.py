from django.db import models
from django.utils import timezone

# Create your models here.
class employees(models.Model):
    
    emp_id = models.CharField(max_length=30)
    emp_name = models.CharField(max_length=50)
    emp_email = models.EmailField(max_length=50)
    emp_phone_no = models.BigIntegerField()
    emp_doj = models.DateField()
    emp_dob = models.DateField()
    emp_job_title = models.CharField(max_length=20)
    emp_address = models.TextField()
    updated_at = models.DateField(default=timezone.now)

class attendance(models.Model):

    user_id = models.IntegerField()
    employee_id = models.IntegerField()
    time_in = models.DateTimeField()
    time_out = models.DateTimeField(default=timezone.now) 
    is_timed_out = models.CharField(max_length=10,default='no')  

 

