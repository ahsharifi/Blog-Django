from django.shortcuts import render

def index(request):

  data = [
    {
      "id": 1,
      "name": "Item1",
      "category": "category1",
      "price": 10000
    },
    {
      "id": 2,
      "name": "Item2",
      "category": "category1",
      "price": 20000
    },
    {
      "id": 3,
      "name": "Item3",
      "category": "category2",
      "price": 33000
    }
  ]

  return render(request, 'shop/index.html', { 'products': data })
