import json

from django.contrib.auth import authenticate, login
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.views import APIView

from books.forms import UserForm
from books.views import UserApi


def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = UserApi({"username":username,"passowrd":password})
        if user is not None:
            login(request,user)
            return redirect('home.html')
        else:
            return HttpResponse("Error logging in")
    else:
        login_form = UserForm()
        return render(request,'home.html',{"login_form":login_form})