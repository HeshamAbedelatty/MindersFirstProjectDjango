from django.contrib import admin
from django.urls import include, path
from .views import show_all_employees

urlpatterns = [
    path("employee/",show_all_employees ,name= "show"),
    
]