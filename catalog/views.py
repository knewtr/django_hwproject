from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)

from catalog.forms import ProductForm, ProductModerForm
from catalog.models import Category, Contact, Product
from catalog.services import get_products_by_category


class ContactsView(View):
    model = Contact

    def get(self, request):
        return render(request, "catalog/contacts.html")

    # def post(self, request, *args, **kwargs):
    #     return render(request, "catalog/contacts/test_form.html")


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})

    def get_form_class(self):
        user = self.request.user
        if self.object.owner == user:
            return ProductForm
        if user.has_perms(["products.can_unpublish_product"]):
            return ProductModerForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")

    def get_form_class(self):
        user = self.request.user
        if self.object.owner == user:
            return ProductForm
        if user.has_perms(["products.can_delete_product"]):
            return ProductModerForm
        raise PermissionDenied


class CategoryDetailView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "catalog/products_list_by_category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.object.pk
        context["products"] = get_products_by_category(pk)
        return context
