from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.fib_nums, name ='fib_nums'),

]