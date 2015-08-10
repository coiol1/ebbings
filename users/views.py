from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from index.models import UserProfile

# Create your views here.
def index(request):
    return render(request, 'users/index.html', {})

def register_teacher(request):
    return render(request, 'users/register_teacher.html', {})

def register_student(request):
    return render(request, 'users/register_student.html', {})

def register_teacher_check(request):
    new_user = User.objects.create_user(username = request.POST.get('username'), password = request.POST.get('password'), email = request.POST.get('email'), first_name = request.POST.get('first_name'), last_name = request.POST.get('last_name'))
    new_up = UserProfile.objects.create(user = new_user, teacher_id = request.POST.get('teacher_id'))
    return render(request, 'users/register_teacher_check.html', {'new_user': new_user})

def register_student_check(request):
    new_user = User.objects.create_user(username = request.POST.get('username'), password = request.POST.get('password'), email = request.POST.get('email'), first_name = request.POST.get('first_name'), last_name = request.POST.get('last_name'))
    new_up = UserProfile.objects.create(user = new_user, student_id = request.POST.get('student_id'))
    return render(request, 'users/register_student_check.html', {'new_user': new_user})