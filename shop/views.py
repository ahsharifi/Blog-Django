from django.shortcuts import render
from shop.models import Product

def index(request):
  data = Product.objects.all()

  return render(request, 'shop/index.html', { 'products': data })

def details(request, slug):

  selected = Product.objects.get(slug = slug)

  return render(request, 'shop/details.html', { "product": selected })
