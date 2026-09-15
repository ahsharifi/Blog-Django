from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('details/<str:slug>', views.details)
]
