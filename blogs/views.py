from django.shortcuts import render
from blogs.models import Blog

def index(request):
  data = Blog.objects.all()
  return render(request, 'blogs/index.html', { "posts": data })

def details(request, id):
  detail = {}

  for item in data:
    if item["id"] == id:
      detail = item
      break

  return render(request, 'blogs/details.html', {"data": detail})