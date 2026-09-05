from django.shortcuts import render
from blogs.models import Blog

def index(request):
  data = Blog.objects.all()
  return render(request, 'blogs/index.html', { "posts": data })

def details(request, id):
  detail = Blog.objects.get(id = id)

  return render(request, 'blogs/details.html', {"data": detail})