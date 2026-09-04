from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('blog-details/<int:id>', views.details)
]
