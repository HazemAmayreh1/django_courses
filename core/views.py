from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Taken')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            user_login = auth.authenticate(username=username, password=password)
            auth.login(request, user_login)
            user_model = User.objects.get(username=username)
            new_student = Students.objects.create(user=user_model, id=user_model.id)
            new_student.save()
            return redirect('/')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    colleges = Colleges.objects.all()
    return render(request,'home.html',{'colleges':colleges})

@login_required(login_url='login')
def search(request):
    courses=Courses.objects.all()
    if request.method == 'POST':
        search_query = request.POST['search']
        courses = Courses.objects.filter(Q(name__icontains=search_query))
    return render(request,'search.html',{'courses':courses})

@login_required(login_url='login')
def addCourse(request,pk):
    course = Courses.objects.get(code=pk)
    student = Students.objects.get(user=request.user)
    if studentsReg.objects.filter(course_id=course,student_id=student).exists():
        return redirect(f'/course/{pk}')
    elif len(studentsReg.objects.filter(course_id=course)) >= course.capacity:
        return redirect(f'/course/{pk}')
    else:
        schedule_new_course = course.schedule_id.start_time
        if studentsReg.objects.filter(student_id=student, course_id__schedule_id__start_time=schedule_new_course).exists():
            return redirect(f'/course/{pk}')
        else:
            studentsReg.objects.create(course_id=course, student_id=student)
            return redirect(f'/course/{pk}')
@login_required(login_url='login')
def deleteCourse(request,pk):
    course = Courses.objects.get(code=pk)
    student = Students.objects.get(user=request.user)
    studentsReg.objects.get(course_id=course,student_id=student).delete()
    return redirect(f'/course/{pk}')
@login_required(login_url='login')
def courseInfo(request,pk):
    course = Courses.objects.get(code=pk)
    student = Students.objects.get(user=request.user)
    regesterd = False
    if studentsReg.objects.filter(course_id=course,student_id=student).exists():
        regesterd = True
    return render(request,'course-info.html',{'course':course,'registered':regesterd,'student_count':len(studentsReg.objects.filter(course_id=course))})
@login_required(login_url='login')
def collegeCourses(request,pk):
    college = Colleges.objects.get(id=pk)
    courses = Courses.objects.filter(college=college)
    return render(request,'college.html',{'college':college,'courses':courses})

@login_required(login_url='login')
def myCourses(request):
    student= Students.objects.get(user=request.user)
    my_courses=studentsReg.objects.filter(student_id=student)
    courses =[]
    for course in my_courses:
        courses.append(course.course_id)
    return render(request,'my-courses.html',{'courses':courses})

