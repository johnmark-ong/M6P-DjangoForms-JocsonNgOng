from django.shortcuts import render, redirect
from .models import Supplier, WaterBottle, Account
from django.contrib import messages

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

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        account = Account.objects.filter(username=u, password=p).first()
        if account: 
            return redirect('view_supplier')
        else: 
            messages.error(request, 'Invalid login')
    
    return render(request, 'MyInventoryApp/login.html')

def signup_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        if Account.objects.filter(username=u).exists():
            messages.warning(request, "Account already exists")
        else:
            Account.objects.create(username=u, password=p)
            messages.success(request, "Account created successfully")
            return redirect('login')
            
    return render(request, 'MyInventoryApp/signup.html')