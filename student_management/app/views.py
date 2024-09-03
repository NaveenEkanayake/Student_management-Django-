from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Student
from django.contrib.auth import authenticate, login

def index(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if email == 'admin123@gmail.com' and password == 'admin123':
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('allstudent')
            else:
                # Redirect back to index without message
                return render(request, "index.html")
        else:
            # Redirect back to index without message
            return render(request, "index.html")

    return render(request, "index.html")

def Allstudent(request):
    data = Student.objects.all()
    context = {"data": data}
    return render(request, "allstudent.html", context)

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        query = Student(name=name, email=email, age=age, gender=gender)
        query.save()
        messages.info(request,"Student added successfully!")
        return redirect('allstudent')

def UpdateData(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        
        student.name = name
        student.email = email
        student.age = age
        student.gender = gender
        student.save()
        messages.warning(request,"Student Updated successfully!")
        return redirect("allstudent")
    
    context = {"d": student}
    return render(request, "Edit.html", context)

def DeleteData(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    messages.error(request,"Student Deleted successfully!")
    return redirect("allstudent")
