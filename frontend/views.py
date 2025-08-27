from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'frontend/index.html')

def login_page(request):
    return render(request, 'frontend/login.html')

def register_page(request):
    return render(request, 'frontend/register.html')

def products_page(request):
    return render(request, 'frontend/products.html')

def cart_page(request):
    return render(request, 'frontend/cart.html')

# @login_required
def profile_page(request):
    return render(request, 'frontend/profile.html')

# @login_required
def orders_page(request):
    return render(request, 'frontend/orders.html')

def admin_dashboard(request):
    return render(request, 'frontend/admin.html')