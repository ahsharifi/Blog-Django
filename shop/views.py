from django.shortcuts import render

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

def index(request):
  return render(request, 'shop/index.html', { 'products': data })

def details(request, id):

  selected = {}

  for item in data:
    if item["id"] == id:
      selected = item
      break

  return render(request, 'shop/details.html', { "product": selected })
