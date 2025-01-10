from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactsView, ProductDetailView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", ContactsView.as_view(), name="contacts"),
    # path("contacts/test_form/", FeedbackView.as_view(), name="test_form"),
    path("", ProductListView.as_view(), name="products_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="products_detail"),
]
