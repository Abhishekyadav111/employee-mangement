
from django import db
from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class username(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    studentcardnumber = models.CharField(max_length=70)
    email=models.CharField(max_length=50) 
    age=models.CharField(max_length=5)
    phone=models.IntegerField()
 
    class mate:
        db_table ='user_info'


class Teacher(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    teacheridnamber=models.CharField(max_length=70)
    email=models.CharField(max_length=50) 
    age=models.CharField(max_length=5)
    phone=models.IntegerField()
 
    class mate:
        db_table =' Teacher_info'



class employee(models.Model):
  id=models.AutoField(primary_key=True)
  name=models.CharField(max_length=50)
  lastname=models.CharField(max_length=50)
  employeeidnamber=models.CharField(max_length=70, default="ram")
  email=models.CharField(max_length=50) 
  # username=models.ForeignKey(username,on_delete=models.CASCADE)
  age=models.CharField(max_length=5)
  phone=models.IntegerField()

  class mate:
      db_table ='employee_info'

class busname(models.Model):
  id=models.AutoField(primary_key=True)
  name=models.CharField(max_length=50)
  # user_in_id = models.ForeignKey('username', on_delete=models.CASCADE) 
  busno = models.CharField(max_length=70)
  


  class mate:
    db_table ='bus_table_info'    



class maintenanceinfo (models.Model):
  id= models.AutoField(primary_key=True) 
  drivename= models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  busno = models.CharField(max_length=70)
  foltpartname= models.CharField(max_length=70)
  phone= models.IntegerField()
  Rs =  models.IntegerField()


  class mate:
    db_table ='maintenance_info'   