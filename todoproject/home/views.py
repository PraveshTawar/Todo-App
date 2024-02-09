from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import todolist

# Create your views here.
def signup_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('pass')
        my_user = User.objects.create_user(username,email,password)
        my_user.save()
        return redirect(login_page)
    return render(request,"signup.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect(todo_page)
        else:
            return redirect(login_page)
    return render(request,"login.html")


@login_required(login_url='/')
def todo_page(request):
    if request.method == "POST":
        data = request.POST.get('text')
        # print(data)
        todo = todolist(task =data,user=request.user)
        # print(request.user)
    
        todo.save()
        # print(res)
        # result=todolist.objects.filter(user=request.user)

        return redirect(todo_page)
    res = todolist.objects.filter(user=request.user)
    return render(request,"index.html",{"res":res}) 

def logout_page(request):
    logout(request)
    return redirect(login_page)

def delete_todo(request,id):
    obj = todolist.objects.get(id=id)
    obj.delete()
    return redirect(todo_page)


def update_todo(request):
    id = request.GET.get('id')
    obj = todolist.objects.get(id=id)
    obj.is_completed = not obj.is_completed
    obj.save()
    return redirect(todo_page)


def edit_todo(request,id):
    
        e = todolist.objects.get(pk=id)
        context = {'e':e}
        # e.task = data
        e.save()
        # return redirect(todo_page,context)

    
    
        return render(request,"edit.html",context)

def edit_done(request,id):
    if request.method == "POST":
        data = request.POST.get("text")
        e=todolist.objects.get(pk=id)
        e.task = data
        e.save()
        return redirect(todo_page)
    return render(request,"edit.html")
