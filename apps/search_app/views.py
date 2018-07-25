from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'search_app/index.html')
