from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    absolute_url = serializers.Field(source='get_absolute_url')

    class Meta:
        model = Product
        filter_fields = ('code',)
        exclude = (
            'allowed_suppliers',
        )
