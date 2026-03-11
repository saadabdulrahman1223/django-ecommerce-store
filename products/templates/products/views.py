def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, "products/product_detail.html", {"product": product})
