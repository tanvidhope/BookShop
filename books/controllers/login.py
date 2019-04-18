import json

from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.views import APIView

from books.forms import UserForm
from books.views import UserApi


def log_in(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = UserApi(request)
        if user is not None:
            login(request,user)
            return redirect('home.html')
        else:
            return HttpResponse("Error logging in")
    else:
        login_form = UserForm()
        return render(request,'registration/login.html',{"form":login_form})


def log_out(request):
        logout(request)
        return redirect(request,'home.html')
