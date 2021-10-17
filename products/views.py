from django.shortcuts import render
from .models import Product
from django.views.generic import ListView,DetailView

class ProductListView(ListView):
    model = Product
    template_name = "products/list_display.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/detail_display.html"


# class ProductFeaturedListView(ListView):
#     model = Product
#     template_name = 'products/featured.html'
#     def get_queryset(self):
#         return Product.objects.all().featured()
    
# class ProductFeaturedDetailView(DetailView):
#     model = Product
#     template_name = 'products/detail_featured.html'
#     def get_queryset(self):
#         return Product.objects.featured()

class ProductSlugDetailView(DetailView):
    model = Product
    template_name = "products/detail_display.html"
