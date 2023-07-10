from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views_packs.product_views.product_views import ProductDeleteView, ProductDetailView, ProductCreateView, ProductUpdateView
from catalog.views import HomepageListView, contacts, Current_ProductDetailView, change_version
from catalog.views_packs.client_views.client_views import ClientListView, ClientUpdateView, ClientCreateView, ClientDeleteView
from catalog.views_packs.blog_views.blog_views import BlogPostListView, BlogPostCreateView, BlogPostDetailView, BlogPostDeleteView, BlogPostUpdateView

app_name = CatalogConfig.name


urlpatterns = [
    path('', HomepageListView.as_view(), name='homepage'),
    path('contacts/', contacts, name='contacts'),
    path('current_prod', cache_page(60)(Current_ProductDetailView.as_view()), name='current_prod'),

    path('clients/', ClientListView.as_view(), name='clients'),
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='clients_update'),
    path('clients/create/', ClientCreateView.as_view(), name='clients_create'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='clients_delete'),

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
