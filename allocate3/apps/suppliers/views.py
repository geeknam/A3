from django.views.generic import TemplateView

from rest_framework import viewsets

from .models import Supplier
from .serializers import SupplierSerializer

class SupplierListView(TemplateView):
    template_name = 'suppliers/supplier_list.html'


class SupplierViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    paginate_by = 10
