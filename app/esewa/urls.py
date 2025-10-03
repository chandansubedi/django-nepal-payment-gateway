from django.contrib import admin
from django.urls import path,include
from app.product.views import *
from .views import *

urlpatterns = [
    path('success/<int:id>', success, name='success'),
    path('failure/<int:id>', failure, name='failure'),


]