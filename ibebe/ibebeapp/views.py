from django.views.generic import ListView, DetailView

from ibebeapp.models import Product, Brand


class ProductListView(ListView):
    model = Product
    template_name = 'ibebe/homepage.html'
    context_object_name = 'products'


class BrandListView(ListView):
    model = Brand
    template_name = 'ibebe/brands.html'
    context_object_name = 'brands'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_url'] = 'https://res.cloudinary.com/dariku/image/upload/v1608215316/ibebe/images/brands'
        return context


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'ibebe/brand-detail.html'
    context_object_name = 'brand'

