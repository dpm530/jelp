from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.db.models import Count
from .models import Business, Review
from ..search_app.models import Location, Search
from ..user_app.models import User

def flashErrors(request,errors):
    for error in errors:
        messages.error(request,error)

def index(request):
    return render(request,'business_app/index.html')

def createBusiness(request):
    if request.method=='POST':
        errors=Business.objects.businessValidation(request.POST)
        if not errors:
            current_user=User.objects.currentUser(request)
            location=Location.objects.existsorcreate(request.POST)
            location_object=Location.objects.get(id=location.id)
            search=Search.objects.existsorcreate(request.POST)
            search_object=Search.objects.get(id=search.id)
            business=Business.objects.createBusiness(request.POST, current_user, location_object, search_object)

            route = "/business/show/{}".format(business.id)
            return redirect(route)

        flashErrors(request,errors)

    return redirect('/business')

def createReview(request,business_id):
    if request.method=='POST':
        errors=Review.objects.reviewValidation(request.POST)
        if not errors:
            current_user=User.objects.currentUser(request)
            business=Business.objects.get(id=business_id)
            review=Review.objects.newReview(request.POST,current_user,business)

            route = "/business/show/{}".format(business.id)
            return redirect(route)

        flashErrors(request,errors)

    return redirect('/user/profile')


def business(request,business_id):
    current_user=User.objects.currentUser(request)
    business=Business.objects.get(id=business_id)
    reviews=business.business_reviewed.all()
    context={
        'user': current_user,
        'business':business,
        'reviews':reviews,
    }


    return render(request,'business_app/business.html', context)
