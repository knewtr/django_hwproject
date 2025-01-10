from django.shortcuts import render
from django.views.generic import DetailView, ListView, View

from catalog.models import Contact, Product


class ContactsView(View):
    model = Contact

    def get(self, request):
        return render(request, "catalog/contacts.html")

    # def post(self, request, *args, **kwargs):
    #     return render(request, "catalog/contacts/test_form.html")


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
