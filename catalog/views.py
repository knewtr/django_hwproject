from django.shortcuts import get_object_or_404, redirect, render

from catalog.models import Product


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return redirect("test_form")
    return render(request, "contacts.html")


def test_form(request):
    return render(request, "test_form.html")


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products_list.html", context=context)


def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "products_detail.html", context=context)
