from rest_framework import viewsets
from .serializers import SupplierSerializer
from .models import Supplier


class SupplierViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    paginate_by = 10
