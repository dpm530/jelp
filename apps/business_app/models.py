from __future__ import unicode_literals

from django.db import models
from ..search_app.models import Location, Search
from ..user_app.models import User

class BusinessManager(models.Manager):

    def businessValidation(self,form_data):
        errors=[]
        if len(form_data['name'])==0:
            errors.append('Name is required.')
        if len(form_data['address'])==0:
            errors.append('Address is required.')
        if len(form_data['city'])==0:
            errors.append('City is required.')
        if len(form_data['state'])==0:
            errors.append('State is required.')
        if len(form_data['number'])==0:
            errors.append('Number is required.')
        if len(form_data['description'])==0:
            errors.append('Description is required.')

        return errors


    def createBusiness(self,form_data,user,location,search):
        business=Business.objects.create(
            name = form_data['name'],
            address = form_data['address'],
            number = form_data['number'],
            description = form_data['description'],
            user = user,
            location = location,
            search = search,
        )
        return business



class ReviewManager(models.Manager):

    def reviewValidation(self,form_data):
        errors=[]
        if len(form_data['comment'])==0:
            errors.append('Content is required.')
        if not(form_data['rating']):
            errors.append('Rating is required.')


        return errors

    def newReview(self,form_data,user,business):
        review=Review.objects.create(
            comment=form_data['comment'],
            rating=form_data['rating'],
            user=user,
            business=business,
        )

        return review


class Business(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, null=True)
    location = models.ForeignKey(Location, related_name="business_location")
    search = models.ForeignKey(Search, related_name="business_search")
    user = models.ForeignKey(User, related_name="business_user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=BusinessManager()
    def __repr__(self):
        return "<Business object: {} {}>".format(self.name, self.address, self.number, self.description, self.location, self.search, self.user)



class Review(models.Model):
    comment = models.TextField(max_length=2000, null=True)
    rating = models.IntegerField(null=True)
    business = models.ForeignKey(Business, related_name="business_reviewed")
    user = models.ForeignKey(User, related_name="user_review")
    objects=ReviewManager()
    def __repr__(self):
        return "<Business object: {} {}>".format(self.comment, self.rating, self.business, self.user)
