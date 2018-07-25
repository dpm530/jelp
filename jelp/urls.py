from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.search_app.urls')),
    url(r'^business', include('apps.business_app.urls')),
    url(r'^user', include('apps.user_app.urls')),
]
