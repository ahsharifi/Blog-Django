from django.shortcuts import render

data = [
  {
    "id": 1,
    "title": "Understanding the request/response cycle",
    "image": "request-cycle.svg",
    "description": "From URL resolver to middleware to view — what actually happens between a click and a rendered template.",
    "category": "Django",
    "tags": ['middleware', 'request', 'view'],
    "author": "ahsharifi",
    "date": "Aug 18 - 6 min",
  },
  {
    "id": 2,
    "title": "Designing a blog schema you won't regret",
    "image": "models.svg",
    "description": "Slugs, timestamps, drafts and relations — small decisions in models.py that pay off months later.",
    "category": "Models",
    "tags": ['models', 'schema'],
    "author": "ahsharifi",
    "date": "Aug 13 - 6 min",
  },
  {
    "id": 3,
    "title": "How to use Django's built-in authentication",
    "image": "templates.svg",
    "description": "Django comes with a robust authentication system. Here's how to use it in your project.",
    "category": "Authentication",
    "tags": ['authentication', 'login', 'user'],
    "author": "ahsharifi",
    "date": "Aug 12 - 6 min",
  },
]

def index(request):
  return render(request, 'blogs/index.html', { "posts": data })

def details(request, id):
  detail = {}

  for item in data:
    if item["id"] == id:
      detail = item
      break

  return render(request, 'blogs/details.html', {"data": detail})