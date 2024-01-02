from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('product/<int:pk>',views.product,name='product'),
    path('cart/',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('thanks',views.thanks,name='thanks'),
    path('register',views.register,name='register'),
    path('forgotpass',views.forgotpass,name='forgotpass'),
]