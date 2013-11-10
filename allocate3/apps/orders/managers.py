from django.db import models
from products.models import Product


class ManifestManager(models.Manager):

    def bulk_create_products(self, data):
        """
        data - list of dicts containing product data
        """
        products = []
        for entry in data:
            products.append(Product(**entry))
        Product.objects.bulk_create(products)

