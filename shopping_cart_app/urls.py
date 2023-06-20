from django.urls import path
from . import views

app_name = "shopping_cart_app"

urlpatterns = [
    path("add/<product_id>/", views.add_product, name="add"),
    path("del/<product_id>/", views.del_product, name="del"),
    path("del_one/<product_id>/", views.del_one_product, name="del_one"),
    path("del_all/", views.del_all_product, name="del_all"),
]
