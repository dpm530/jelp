from __future__ import unicode_literals

from django.db import models


class LocationManager(models.Manager):

    def existsorcreate(self,form_data):
        obj, location = Location.objects.get_or_create(
            city=form_data['city'],
            state=form_data['state'],
        )

        return obj




class Search(models.Model):
    category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LocationManager()
    def __repr__(self):
        return "<Search object: {} {}>".format(self.category)

class Location(models.Model):
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=LocationManager()
    def __repr__(self):
        return "<Location object: {} {}>".format(self.city, self.state)
