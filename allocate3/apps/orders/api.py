from rest_framework import viewsets, filters
from .models import Manifest, Invoice, InvoiceLine
from .serializers import ManifestSerializer, InvoiceSerializer, InvoiceLineSerializer


class ManifestViewSet(viewsets.ModelViewSet):
    queryset = Manifest.objects.all()
    serializer_class = ManifestSerializer

    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
    search_fields = ('name', 'slug')
    filter_fields = ('status',)
    paginate_by = 10


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('order_number', 'email', 'internal_reference')
    paginate_by = 10


class InvoiceLineViewSet(viewsets.ModelViewSet):
    queryset = InvoiceLine.objects.all()
    serializer_class = InvoiceLineSerializer
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
    search_fields = ('product__name', 'invoice__name', 'invoice__email')
    filter_fields = ('invoice__manifest__slug', 'supplier__name')
    paginate_by = 10
