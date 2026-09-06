from django.shortcuts import render
from shop.models import Product

def index(request):
  data = Product.objects.all()

  return render(request, 'shop/index.html', { 'products': data })

def details(request, id):

  selected = Product.objects.get(id = id)

  return render(request, 'shop/details.html', { "product": selected })
