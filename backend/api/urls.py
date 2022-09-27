from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *
from rest_framework import permissions

# all api endpoints
urlpatterns = [
    path('test/', Test.as_view()),
    path('test2/', Test2.as_view()),
]