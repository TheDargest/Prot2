from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProject, Role, Department, Category, Task, Status


# Create your views here.

def home(request):
    user_id = request.user.id
    tasks = Task.objects.filter(id_user=user_id).order_by('-id')

    return render(request, 'app1/home.html', {'tasks': tasks})



def register(request):
        if request.method == 'POST':

            username = request.POST.get('username')
            FIO = request.POST.get('FIO')
            department_id = request.POST.get('department')
            email_form = request.POST.get('mail')
            password = request.POST.get('password')
            phone = request.POST.get('phone')
            id_role = Role.objects.get(id=1)

            print(f'ФИО: {FIO} department_id: {department_id} email_form: {email_form} password: {password} phone: {phone}')

            department = Department.objects.get(id=department_id)

            if User.objects.filter(username=username):
                messages.success(request, "Пользователь с таким логином уже был создан")
                return redirect('reg')

            if User.objects.filter(email=email_form):
                messages.success(request, "Пользователь с такой почтой уже был создан")
                return redirect('register')

            userdjango = User.objects.create_user(username=username, email=email_form, password=password)
            usercreate = UserProject(full_name=FIO, phone=phone, email=email_form, password="encrypted(см. auth_user)", id_department=department, id_role=id_role)
            usercreate.save()

            userdjangologin = authenticate(request, username=username, password=password)
            if userdjangologin is not None:
                login(request, userdjangologin)
                return redirect('home')
        departments = Department.objects.all()
        return render(request, 'app1/register.html', {'departments': departments})


def loging_in(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(f'username: {username} password: {password}')
            userdjangologin = authenticate(request, username=username, password=password)

            if userdjangologin is not None:
                login(request, userdjangologin)
                messages.success(request, "Вы вошли в систему")
                return redirect('home')
            else:
                messages.success(request, "Вы не вошли в систему")
                return render(request, 'app1/login.html')

        return render(request, 'app1/login.html')

def logging_out(request):
    logout(request)
    messages.success(request, "Вы вышли из системы")
    return redirect('home')


def task(request):

    if request.method == 'POST':
        category_id = request.POST.get('category')
        # category_id = Category.objects.get(id=category_id)
        task_message = request.POST.get('task_message')
        print(f'category_id: {category_id} task_message: {task_message} request.user.id {request.user.id}')
        user_id = User.objects.get(id=request.user.id)
        category_id = Category.objects.get(id=category_id)
        print(f'user_id: {user_id}')

        TaskCreate = Task(id_user = user_id, id_category = category_id, id_status = Status.objects.get(id=1), description = task_message)
        TaskCreate.save()
        messages.success(request, "Заявка успешно создана")
        return redirect('home')

    categories = Category.objects.all()
    return render(request, 'app1/zayavka.html', {'categories': categories})

