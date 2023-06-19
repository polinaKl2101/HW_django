from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomepageListView, contacts, Current_prodDetailView, BlogPostListView, ProductCreateView, \
    ProductUpdateView, BlogPostCreateView, BlogPostDetailView, change_version

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomepageListView.as_view(), name='homepage'),
    path('contacts/', contacts, name='contacts'),
    path('current_prod', Current_prodDetailView.as_view(), name='current_prod'),
    path('blog_post/', BlogPostListView.as_view(), name='blog_post'),
    path('detail_blogpost/', BlogPostDetailView.as_view(), name='detail_blogpost'),
    path('create_blogpost/', BlogPostCreateView.as_view(), name='create_blogpost'),
    path('delete_blogpost/', BlogPostCreateView.as_view(), name='delete_blogpost'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('change_version/<int:product_id>/', change_version, name='change_version'),
]
