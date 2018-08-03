from __future__ import unicode_literals
import bcrypt
from django.db import models
from ..search_app.models import Location




class UserManager(models.Manager):

    def currentUser(self, request):
        id=request.session['user_id']

        return User.objects.get(id=id)

    def validateUser(self,form_data):
        errors=[]
        if len(form_data['name'])==0:
            errors.append('Name is Required.')
        if len(form_data['email'])==0:
            errors.append('Email is Required.')
        if len(form_data['password'])==0:
            errors.append('Password is Required.')
        if len(form_data['city'])==0:
            errors.append('City is Required.')
        if len(form_data['state'])==0:
            errors.append('State is Required.')


        return errors

    def createUser(self,form_data):
        location=Location.objects.existsorcreate(form_data)
        location_object=Location.objects.get(id=location.id)
        password=str(form_data['password'])
        hashed_pw=bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        user=User.objects.create(
            name=form_data['name'],
            email=form_data['email'],
            password=hashed_pw,
            location=location_object,
        )

        return user

    def validateLogin(self,form_data):
        errors=[]

        if len(form_data['email'])==0:
            errors.append('Email is Required.')
        if len(form_data['password'])==0:
            errors.append('Password is Required.')

        return errors



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    location = models.ForeignKey(Location, related_name='user_location', null='TRUE', blank='TRUE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()
    def __repr__(self):
        return "<User object: {} {}>".format(self.name, self.email, self.location_id)
