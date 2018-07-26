from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^createBusiness$',views.createBusiness),
    url(r'^show/(?P<business_id>\d+)$',views.business),
    url(r'^createReview/(?P<business_id>\d+)$',views.createReview),
]
