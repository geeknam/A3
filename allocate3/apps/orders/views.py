from django.views.generic import TemplateView, CreateView
from .models import Manifest
from core.views import BreadcrumbsMixin


class ManifestListView(BreadcrumbsMixin, TemplateView):
    template_name = 'orders/manifest_list.html'


class ManifestCreateView(BreadcrumbsMixin, CreateView):
    model = Manifest

    def get_breadcrumbs(self, *args, **kwargs):
        return [('Create New Manifest', '')]