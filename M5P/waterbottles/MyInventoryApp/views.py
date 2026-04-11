from django.shortcuts import get_object_or_404, render, redirect
from .models import Supplier, WaterBottle, Account
from django.contrib import messages

current_account = None
# Create your views here.
def view_bottles(request):
    waterbottle_objects = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {'waterbottles':waterbottle_objects})

def view_supplier(request):
    supplier_objects = Supplier.objects.all()
    return render(request, 'MyInventoryApp/view_supplier.html', {
        'suppliers':supplier_objects,
        'account': current_account,
        })

def view_inventory(request):
    #waterbottle_objects = WaterBottle.objects.all(), {'waterbottles':waterbottle_objects}
    return render(request, 'MyInventoryApp/base.html')

def add_bottle(request):
    if request.method == 'POST':
        sku = request.POST.get('sku')
        brand = request.POST.get('brand')
        cost = request.POST.get('cost')
        size = request.POST.get('size')
        mouth_size = request.POST.get('mouth_size')
        color = request.POST.get('color')
        supplier_id = request.POST.get('supplier')
        quantity = request.POST.get('quantity')

        supplier = get_object_or_404(Supplier, pk=supplier_id)
        WaterBottle.objects.create(
            SKU=sku,
            Brand=brand,
            Cost=cost,
            Size=size,
            Mouth_Size=mouth_size,
            Color=color,
            Supplied_by=supplier,
            Current_Quantity=quantity,
        )
        return redirect('view_supplier')
    
    suppliers = Supplier.objects.all()
    return render(request, 'MyInventoryApp/add_bottle.html', {'suppliers': suppliers})

def login_view(request):
    global current_account
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        account = Account.objects.filter(username=u, password=p).first()
        if account: 
            current_account = account
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

def logout_view(request):
    global current_account
    current_account = None
    return redirect('login')

def view_bottle_details(request, pk):
    bottle = get_object_or_404(WaterBottle, pk=pk)
    return render(request, 'MyInventoryApp/bottle_detail.html', {'bottle': bottle})

def delete_bottle(request, pk):
    WaterBottle.objects.filter(pk=pk).delete()
    return redirect('view_bottles')

def manage_account(request, pk):
    account = get_object_or_404(Account, pk=pk)
    return render(request, 'MyInventoryApp/manage_account.html', {'account': account})

def delete_account(request, pk):
    global current_account
    Account.objects.filter(pk=pk).delete()
    current_account = None
    return redirect('login')

def change_password(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        current_pw = request.POST.get('current_password')
        new_pw = request.POST.get('new_password')
        confirm_pw = request.POST.get('confirm_password')

        if current_pw != account.password():
            messages.error(request, "Current password is incorrect. Please try again.")
        elif new_pw != confirm_pw:
            messages.error(request, "New password and confirmation do not match. Please try again.")
        else:
            Account.objects.filter(pk=pk).update(password=new_pw)
            messages.success(request, "Password updated successfully.")
            return redirect('manage_account', pk=pk)
        
    return render(request, 'MyInventoryApp/change_password.html', {'account': account})