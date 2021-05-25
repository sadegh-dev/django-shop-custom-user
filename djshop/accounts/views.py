from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User


def home(request):
    return render(request, 'accounts/home.html')



def user_register(request):
    if request.method == 'POST' :
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['email'],cd['full_name'],cd['password'])
            user.save()
            login(request,user)
            messages.success(request, 'you registered successfully' , 'success')
            return redirect('accounts:home')
    else:
        form = UserRegistrationForm()
    context = {
        'form' : form ,
    }
    return render(request, 'accounts/register.html', context )



def user_login(request):
    if request.method == 'POST' :
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email = cd['email'], password = cd['password'])
            if user is not None :
                login(request,user)
                messages.success(request, 'you logged in successfully' , 'success')
                return redirect('accounts:home')
            else :
                messages.error(request, 'username or password is wrong', 'danger')
    else:
        form = UserLoginForm()
    context = {
        'form' : form ,
    }
    return render(request, 'accounts/login.html', context )



def user_logout(request):
    logout(request)
    messages.success(request, 'you logged out successfully' , 'success')
    return redirect('accounts:home')




