from django.shortcuts import render
from .models import Product, Category

# Create your views here.

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, 'shop_app/shop.html', {'products': products, 'categories': categories})

def product_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'shop_app/shop.html', {'products': products, 'categories': categories, 'selected_category': category})