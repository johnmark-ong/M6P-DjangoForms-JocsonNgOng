from django.shortcuts import render, redirect
from .models import Dish, Account
from django.contrib import messages

# Create your views here.

def view_basic_list(request):
    dish_objects = Dish.objects.all()
    return render(request, 'tapasapp/basic_list.html', {'dishes':dish_objects})


def view_menu(request):
    dish_objects = Dish.objects.all()
    return render(request, 'tapasapp/list.html', {'dishes':dish_objects})

def add_menu(request):
    return render(request, 'tapasapp/add_menu.html')