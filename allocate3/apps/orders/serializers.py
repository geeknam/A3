from .models import Manifest, Invoice, InvoiceLine
from rest_framework import serializers
from suppliers.serializers import SupplierSerializer


class ManifestSerializer(serializers.HyperlinkedModelSerializer):
    total_invoices = serializers.Field(source='total_invoices')

    class Meta:
        model = Manifest


class InvoiceLineSerializer(serializers.HyperlinkedModelSerializer):
    supplier = SupplierSerializer()

    class Meta:
        model = InvoiceLine


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    lines = InvoiceLineSerializer(many=True)

    class Meta:
        model = Invoice

