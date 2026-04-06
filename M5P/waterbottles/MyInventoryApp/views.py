from django.shortcuts import render
from .models import Supplier, WaterBottle

# Create your views here.
def view_bottles(request):
    waterbottle_objects = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {'waterbottles':waterbottle_objects})

def view_supplier(request):
    supplier_objects = Supplier.objects.all()
    return render(request, 'MyInventoryApp/view_supplier.html', {'suppliers':supplier_objects})

def view_inventory(request):
    #waterbottle_objects = WaterBottle.objects.all(), {'waterbottles':waterbottle_objects}
    return render(request, 'MyInventoryApp/base.html')

def add_bottle(request):
    return render(request, 'MyInventoryApp/add_bottle.html')