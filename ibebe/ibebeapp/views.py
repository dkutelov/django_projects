from django.views.generic import ListView

from ibebeapp.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'ibebe/homepage.html'
    context_object_name = 'products'
