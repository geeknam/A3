from .models import Supplier
from rest_framework import serializers


class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        filter_fields = ('code',)
