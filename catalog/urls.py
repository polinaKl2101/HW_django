from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import HomepageListView, contacts, Current_ProductDetailView, BlogPostListView, ProductCreateView, \
    ProductUpdateView, BlogPostCreateView, BlogPostDetailView, change_version, ProductDeleteView, BlogPostDeleteView, \
    BlogPostUpdateView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomepageListView.as_view(), name='homepage'),
    path('contacts/', contacts, name='contacts'),
    path('current_prod', cache_page(60)(Current_ProductDetailView.as_view()), name='current_prod'),

    path('blog_post/', BlogPostListView.as_view(), name='blog_post'),
    path('detail_blogpost/<int:pk>/', BlogPostDetailView.as_view(), name='detail_blogpost'),
    path('update_blogpost/<int:pk>/', BlogPostUpdateView.as_view(), name='update_blogpost'),
    path('create_blogpost/', BlogPostCreateView.as_view(), name='create_blogpost'),
    path('delete_blogpost/<int:pk>/', BlogPostDeleteView.as_view(), name='delete_blogpost'),

    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('detail_product/<int:pk>/', ProductDetailView.as_view(), name='detail_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('change_version/<int:product_id>/', change_version, name='change_version'),
]
