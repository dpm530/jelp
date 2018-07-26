from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.db.models import Count
from .models import User
from ..search_app.models import Location
from ..business_app.models import Business
import bcrypt

def flashErrors(request,errors):
    for error in errors:
        messages.error(request,error)

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

            return redirect('/user/profile')

        flashErrors(request,errors)
    return redirect('/user/newUser')

def profile(request):
    current_user=User.objects.currentUser(request)
    business=Business.objects.all().order_by('-created_at')

    context = {
        'user': current_user,
        'business':business,
    }


    return render(request,'user_app/profile.html', context)

def login(request):
    if request.method=='POST':
        errors=User.objects.validateLogin(request.POST)
        if not errors:
            user=User.objects.filter(email=request.POST['email']).first()

            if user:
                password=str(request.POST['password'])
                user_password=str(user.password)

                hashed_pw=bcrypt.hashpw(password,user_password)

                if hashed_pw==user_password:
                    request.session['user_id']=user.id

                    return redirect('/user/profile')

            errors.append('Invalid account Information')
        flashErrors(request,errors)

    return redirect('/user')

def logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id')
    return redirect('/')
