from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Count
from .models import User
from ..search_app.models import Location
import bcrypt

def index(request):
    return render(request,'user_app/index.html')


def newUser(request):
    return render(request,'user_app/newUser.html')

def signup(request):
    if request.method=='POST':
        errors=User.objects.validateUser(request.POST)

        if not errors:
            print 'Create User'
            user=User.objects.createUser(request.POST,)

            request.session['user_id']=user.id

            return redirect('/business')

        flashErrors(request,errors)
    return redirect('/user/signup')
