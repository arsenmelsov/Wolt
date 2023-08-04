from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import auth
from .models import User
from django.contrib import messages
from .forms import *

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/user_detail.html', {'user': user})

def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'users/user_edit.html', {'form': form})

def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_edit.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})

def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.info(request, f'Hello {name}, You are Successfully Registered!!') 
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})

def user_login(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'home')
        else:
            if not User.objects.filter(email=email).exists():
                messages.error(request, "Username Doesn't Exist")
            else:
                messages.info(request, "Incorrect Password")
            return redirect('home')

    else:  
        return render(request, 'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')