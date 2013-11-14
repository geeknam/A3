from django.views.generic import DetailView, TemplateView
from core.views import BreadcrumbsMixin

from .models import Product


class ProductListView(BreadcrumbsMixin, TemplateView):
    template_name = 'products/product_list.html'


class ProductDetailView(DetailView):
    model = Product

