from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)

from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.forms import ProductForm
from catalog.models import Contact, Product


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


class ProductListView(ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
