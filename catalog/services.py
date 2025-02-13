from catalog.models import Product, Category
from django.core.cache import cache
from config.settings import CACHE_ENABLED


class ProductService:

    @staticmethod
    def get_products_from_cache():
        """Функция возвращает данные из кэша или бд"""
        if not CACHE_ENABLED:
            return Product.objects.all()
        key = 'product_list'
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.all()
        cache.set(key, products)
        return products

    @staticmethod
    def get_products_by_category(**kwargs):
        """Функция возвращает список продуктов по заданной категории"""
        category = kwargs.get('name')
        products = Product.objects.filter(category=category)
        return products