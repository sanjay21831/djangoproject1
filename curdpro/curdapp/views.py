from django.shortcuts import render,redirect
from. models import StudentsData
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def homepage(request):
    students=StudentsData.objects.all()
    return render(request,"homepage.html",{'students':students})
#@login_required
def add_student(request):
    
    if request.method =="GET":
        return render(request,'add_student.html')
    else:
        StudentsData(
            fist_name=request.POST.get('fname'),
            last_name=request.POST.get('lname'),
            course=request.POST.get('course'),
            fee=request.POST.get('fee'),
            assigment1=request.POST.get('a1'),
            assigment2=request.POST.get('a2'),
            assigment3=request.POST.get('a3'),
            assigment4=request.POST.get('a4'),
            institute=request.POST.get('institute'),
           location=request.POST.get('location')
        ) .save()
        return render(request,'add_student.html')
    #return HttpResponse('thanku')
#@login_required
def update_student(request,id):
    student = StudentsData.objects.get(id=id)
    if request.method=='GET':
      return render(request,"update_student.html",{'student':student})
    else:
        student.fist_name=request.POST.get("fname")
        student.last_name=request.POST.get('lname')
        student.course=request.POST.get('course')
        student.fee=request.POST.get('fee')
        student.assigment1=request.POST.get('a1')
        student.assigment2=request.POST.get('a2')
        student.assigment3=request.POST.get('a3')
        student.assigment4=request.POST.get('a4')
        student.institute=request.POST.get('institute')
        student.location=request.POST.get('location')
        student.save()
        return redirect('homepage')
#@login_required(login_url='login')
def delete_student(request,id):
    student=StudentsData.objects.get(id=id)
    student.delete()
    return redirect('homepage')