from django.urls import path
from . import views

urlpatterns = [

    path("", views.product_list, name="product_list"),

    path("product/<int:id>/", views.product_detail, name="product_detail"),

    path("category/<slug:slug>/", views.category_products, name="category_products"),

    path("add-to-cart/<int:id>/", views.add_to_cart, name="add_to_cart"),

    path("remove-from-cart/<int:id>/", views.remove_from_cart, name="remove_from_cart"),

    path("cart/", views.cart, name="cart"),

]