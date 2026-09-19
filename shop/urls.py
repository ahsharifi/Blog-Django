from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products_list'),
    path('details/<str:slug>', views.details, name='product_details'),
    path('create/', views.create_product, name='create_product'),
]
