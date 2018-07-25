from __future__ import unicode_literals

from django.db import models
from ..search_app.models import Location


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    location = models.ForeignKey(Location, related_name='user_location')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Business object: {} {}>".format(self.name, self.email, self.password, self.location)
