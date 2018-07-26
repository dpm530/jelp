from django.shortcuts import render, HttpResponse, redirect

# def flashErrors(request,errors):
#     for error in errors:
#         messages.error(request,error)

def index(request):
    return render(request,'search_app/index.html')
