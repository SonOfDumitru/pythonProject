from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.
def home_page(request):
    return HttpResponse('Hello')


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products.html'

    def get_queryset(self):
        return Product.objects.all


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product.html'


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    fields = '__all__'
    template_name = 'products_form.html'
    success_url = reverse_lazy('products:products')
    permission_required = ('products.add_product',)
