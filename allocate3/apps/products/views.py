from django.views.generic import DetailView, TemplateView

from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer
from rest_framework import filters


class ProductListView(TemplateView):
    template_name = 'products/product_list.html'


class ProductDetailView(DetailView):
    model = Product


# API Views
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('code', 'name')
    paginate_by = 50
