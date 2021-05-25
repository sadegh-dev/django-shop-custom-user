from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, 'accounts/home.html')


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




