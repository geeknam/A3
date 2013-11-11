from .models import Supplier
from rest_framework import serializers


class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    absolute_url = serializers.Field(source='get_absolute_url')

    class Meta:
        model = Supplier
        filter_fields = ('code',)
