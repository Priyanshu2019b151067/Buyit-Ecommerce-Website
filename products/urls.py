from django.urls import path
from .views import (
    ProductDetailView,
    ProductListView,
    # ProductFeaturedListView,
    # ProductFeaturedDetailView,
    ProductSlugDetailView
    )
urlpatterns = [
    path('',ProductListView.as_view(),name='product_list'),
    path('<int:pk>/',ProductDetailView.as_view(),name='product_detail'),
    # path('featured/',ProductFeaturedListView.as_view(),name='featured_list'),
    # path('featured/<int:pk>/',ProductFeaturedDetailView.as_view(),name='featured_detail'),
    path('<slug:slug>',ProductSlugDetailView.as_view(),name='slug_detail')
]
