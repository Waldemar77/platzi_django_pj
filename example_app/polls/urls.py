# file to store the url of our app

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
