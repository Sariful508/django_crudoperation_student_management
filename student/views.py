from django.shortcuts import render,redirect
from .models import student
# Create your views here.
def home(request):
    std=student.objects.all()
    return render(request,"home.html",{'std':std})

def student_add(request):
    if request.method=='POST':
        print("Added")
        std_roll=request.POST.get("student_roll")
        std_name=request.POST.get("student_name")
        std_email=request.POST.get("student_email")
        std_address=request.POST.get("student_address")
        std_phone=request.POST.get("student_phone")

        #create an object for model
        s = student()
        s.roll = std_roll
        s.name = std_name
        s.email = std_email
        s.address = std_address
        s.phone = std_phone

        s.save()
        return redirect("/student/home/")
    return render(request,"add_student.html",{})

def delete_student(requeast,roll):
    s = student.objects.get(pk=roll)
    s.delete()

    return redirect("/student/home")

def update_student(request,roll):
    stds=student.objects.get(pk=roll)
    return render(request,"update_student.html",{'stds':stds})

def do_update_student(request,roll):
     std_roll=request.POST.get("student_roll")
     std_name=request.POST.get("student_name")
     std_email=request.POST.get("student_email")
     std_address=request.POST.get("student_address")
     std_phone=request.POST.get("student_phone")

     std = student.objects.get(pk=roll)
     std.roll=std_roll
     std.name=std_name
     std.email=std_email
     std.address=std_address
     std.phone=std_phone
     std.save()

     return redirect("/student/home")



