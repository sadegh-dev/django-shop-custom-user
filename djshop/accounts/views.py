from django.shortcuts import render

def login(request):
    render (request, 'accounts/login.html')
