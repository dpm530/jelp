from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^newUser$',views.newUser),
    url(r'^signup$',views.signup),
    url(r'^login$',views.login),
    url(r'^profile$',views.profile),
    url(r'^logout$',views.logout),
]
