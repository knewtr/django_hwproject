from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


class ProductService:

    def get_products_by_category(category_id):
        """Функция возвращает список продуктов по заданной категории"""
        products = Product.objects.filter(category=category_id)
        return products

    @staticmethod
    def get_products_from_cache():
        """Функция возвращает данные из кэша или бд"""
        if not CACHE_ENABLED:
            return Product.objects.all()
        key = "product_list"
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.all()
        cache.set(key, products)
        return products
