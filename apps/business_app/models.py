from __future__ import unicode_literals

from django.db import models

from ..user_app.models import User
from ..search_app.models import Search, Location

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
    def __repr__(self):
        return "<Business object: {} {}>".format(self.name, self.address, self.number, self.description, self.location, self.search, self.user)



class Review(models.Model):
    comment = models.TextField(max_length=2000, null=True)
    rating = models.IntegerField(null=True)
    business = models.ForeignKey(Business, related_name="business_reviewed")
    user = models.ForeignKey(User, related_name="user_review")
    def __repr__(self):
        return "<Business object: {} {}>".format(self.comment, self.rating, self.business, self.user)
