from django.shortcuts import render, redirect
from .cart import Cart
from shopping_cart_app.models import Product

# Create your views here.

def add_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product)
    return redirect("virtual_shop")

def del_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.delete(product)
    return redirect("virtual_shop")

def del_one_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.delete_one(product)
    return redirect("virtual_shop")

def del_all_product(request):
    cart = Cart(request)
    cart.delete_all()
    return redirect("virtual_shop")