from django.contrib import admin
from .models import *
# Register your models here.
class usernameadmin(admin.ModelAdmin):
    list_display=['id','name','lastname','studentcardnumber','email','age','phone']

class Teacheradmin(admin.ModelAdmin):
    list_display=['id','name','lastname','teacheridnamber','email','age','phone']

class employeeadmin(admin.ModelAdmin):
    list_display=['id','name','lastname','employeeidnamber','email','age','phone']

class busnameadmin(admin.ModelAdmin):
    list_display=['id','name','busno']    

class maintenanceinfoadmin(admin.ModelAdmin):
    list_display=['id','drivename','lastname','busno','foltpartname','phone','Rs']


admin.site.register (username,usernameadmin)
admin.site.register (Teacher,Teacheradmin)
admin.site.register (employee,employeeadmin)
admin.site.register (busname,busnameadmin)
admin.site.register (maintenanceinfo,maintenanceinfoadmin)

