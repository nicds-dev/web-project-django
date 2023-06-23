from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.shop, name='Shop'),
    path('category/<int:category_id>/', views.product_by_category, name='product_by_category'),
]
