from django.views.generic import TemplateView, DetailView
from core.views import BreadcrumbsMixin
from rest_framework import viewsets

from .models import Supplier
from .serializers import SupplierSerializer


class SupplierListView(TemplateView):
    template_name = 'suppliers/supplier_list.html'


class SupplierDetailView(BreadcrumbsMixin, DetailView):
    model = Supplier
    template_name = 'suppliers/supplier_detail.html'

    def get_object(self):
        return self.get_queryset().get(slug=self.kwargs['slug'])

    def get_breadcrumbs(self, *args, **kwargs):
        supplier = self.get_object()
        return [
            (supplier.name, '')
        ]


class SupplierViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    paginate_by = 10
