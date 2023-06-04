from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomepageListView, contacts, Current_prodDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomepageListView.as_view(), name='homepage'),
    path('contacts/', contacts, name='contacts'),
    path('current_prod', Current_prodDetailView.as_view(), name='current_prod')
]