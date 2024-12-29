from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, products_detail, products_list, test_form

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", contacts, name="contacts"),
    path("contacts/test_form/", test_form, name="test_form"),
    path("", products_list, name="products_list"),
    path("products/<int:pk>/", products_detail, name="products_detail"),
]
