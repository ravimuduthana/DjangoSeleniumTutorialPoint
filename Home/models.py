from django.db import models

# Create your models here.
class Users(models.Model):
    employee_id=models.CharField(max_length=10,null=True,blank=True,unique=True)
    employee_name=models.CharField(max_length=100)
    age=models.IntegerField()
    
    def __str__(self):
        return {self.employee_id}
        