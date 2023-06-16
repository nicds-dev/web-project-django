from django.contrib import admin
from .models import Category, Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)