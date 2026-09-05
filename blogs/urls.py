from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blogs_list'),
    path('blog-details/<int:id>', views.details, name='blogs_details')
]
