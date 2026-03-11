from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Product, Category


def product_list(request):

    query = request.GET.get("q")

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query)
        )
    else:
        products = Product.objects.all()

    categories = Category.objects.all()

    return render(
        request,
        "products/product_list.html",
        {
            "products": products,
            "categories": categories
        }
    )


def category_products(request, slug):

    category = get_object_or_404(Category, slug=slug)

    products = Product.objects.filter(category=category)

    categories = Category.objects.all()

    return render(
        request,
        "products/category_products.html",
        {
            "products": products,
            "category": category,
            "categories": categories
        }
    )


def product_detail(request, id):

    product = get_object_or_404(Product, id=id)

    return render(
        request,
        "products/product_detail.html",
        {"product": product}
    )


def add_to_cart(request, id):

    cart = request.session.get("cart", {})

    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1

    request.session["cart"] = cart

    return redirect("cart")


def remove_from_cart(request, id):

    cart = request.session.get("cart", {})

    if str(id) in cart:
        del cart[str(id)]

    request.session["cart"] = cart

    return redirect("cart")


def cart(request):

    cart = request.session.get("cart", {})

    products = []

    total = 0

    for id, quantity in cart.items():

        product = Product.objects.get(id=id)

        product.quantity = quantity

        product.subtotal = product.price * quantity

        total += product.subtotal

        products.append(product)

    return render(
        request,
        "products/cart.html",
        {
            "products": products,
            "total": total
        }
    )