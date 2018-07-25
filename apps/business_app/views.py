from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'business_app/index.html')
