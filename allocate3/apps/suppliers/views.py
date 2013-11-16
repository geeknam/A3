from django.views.generic import TemplateView, DetailView
from core.views import BreadcrumbsMixin

from .models import Supplier


class SupplierListView(BreadcrumbsMixin, TemplateView):
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
