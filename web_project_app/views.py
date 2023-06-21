from django.shortcuts import render, HttpResponse
from shopping_cart_app.cart import Cart

# Create your views here.

def index(request):
    cart = Cart(request)
    return render(request, 'web_project_app/index.html')

def about(request):
    return render(request, 'web_project_app/about.html')