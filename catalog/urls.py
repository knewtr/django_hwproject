from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, test_form

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('contacts/test_form/', test_form, name='test_form'),
]