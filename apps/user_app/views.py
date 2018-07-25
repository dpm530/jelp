from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Count
from .models import User
from ..search_app.models import Location

def index(request):
    return render(request,'user_app/index.html')


def newUser(request):
    return render(request,'user_app/newUser.html')
