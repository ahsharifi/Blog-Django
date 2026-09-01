from django.shortcuts import render

def index(request):

  data = [
    {
      "name": "Item1",
      "category": "category1",
      "price": 10000
    },
    {
      "name": "Item2",
      "category": "category1",
      "price": 20000
    },
    {
      "name": "Item3",
      "category": "category2",
      "price": 33000
    }
  ]

  return render(request, 'shop/index.html', { 'products': data })
