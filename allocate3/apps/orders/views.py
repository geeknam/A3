from django.views.generic import TemplateView


class ManifestListView(TemplateView):
    template_name = 'orders/manifest_list.html'


