from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('update_product/<int:id>/', views.update_product, name='update_product'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
    path('search_products/', ProductSearchView.as_view(), name='search_products'),
]