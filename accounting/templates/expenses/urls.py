from django.urls import path
from .import views

urlpathterns = [
    path('create/',views.create,name = 'expenses_create')

]