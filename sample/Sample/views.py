import email
from multiprocessing import context
from unicodedata import name
from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import render
from.models import employee,username,Teacher, busname
from django.db.models import Q

from crypt import methods
from wsgiref.util import request_uri
from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request,'index.html')
    

def add_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        employeeidnamber = int(request.POST['employeeidnamber'])
        email = request.POST['email']
        age = int(request.POST['age'])
        phone = int(request.POST['phone'])
        new_emp=employee(name=name,lastname=lastname,employeeidnamber=employeeidnamber,email=email,age=age,phone=phone)
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method == 'GET':
     return render(request,'add_emp.html')
    else:
        return HttpResponse('An EXception occured!Employee Has not beenAdded')

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
           emp_to_be_removed=employee.objects.get(id=emp_id)
           emp_to_be_removed.delete()
           return HttpResponse("Employee added Successfully")
        except :
            return HttpResponse("Please Enter Avalid Emp ID")  

    emps=employee.objects.all()
    
    context={
           'emps':emps,
           
       } 
    return render(request,'remove_emp.html',context)
            
def view_all_emp(request):
    emps=employee.objects.all()
    
    context={
           'emps':emps,
           
       } 
    print(context)
    return render(request,'view_all_emp.html',context)


def filter_emp(request):
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        emps=employee.objects.all()
        if name:
            emps=emps.filter(Q(name__icontains=name) | Q(lastname__icontains=name))
        if email:
            emps= emps.filter(email__name=email)
        if phone:
            emps= emps.filter(phone__name=phone)
        context={
           'emps':emps,
           
       } 
        return render(request,'view_all_emp.html',context)
    elif request.method=='GET':
     return render(request,'filter_emp.html')

    else:
        return HttpResponse('An exception Occurred')
def calculator(request):
    c=''
    
    if request.method=="POST":
        n1=eval(request.POST.get('num1'))
        n2=eval(request.POST.get('num2'))
        opr=request.POST.get('opr')
        if opr=="+":
            c=n1+n2 

        elif opr=="-":
            c=n1-n2 

        elif opr=="*":
            c=n1*n2 

        elif opr=="/":
            c=n1/n2
    
        # print(n1,n2,opr)

        print(c)
       

    # return render(request,"calculator.html")
    return render(request,"calculator.html",{"c":c})
def evenodd(request):
    c=''
    if request.method=="POST":
        n=eval(request.POST.get('num1'))
        if n%2==0:
            c="Even Number"
        else:
            c="odd Number"
    return render(request,"evenodd.html",{'c':c})            