from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, test_message

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('test_message/', test_message, name='test_message'),
]