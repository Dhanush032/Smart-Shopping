from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('products/', views.products_page, name='products'),
    path('cart/', views.cart_page, name='cart'),
    path('profile/', views.profile_page, name='profile'),
    path('orders/', views.orders_page, name='orders'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]