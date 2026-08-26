from django.shortcuts import render

def index(request):

  data = [
    {
      "title": "Understanding the request/response cycle",
      "image": "request-cycle.svg",
      "description": "From URL resolver to middleware to view — what actually happens between a click and a rendered template.",
      "category": "Django",
      "tags": ['middleware', 'request', 'view'],
      "author": "ahsharifi",
      "date": "Aug 18 - 6 min",
    },
    {
      "title": "Designing a blog schema you won't regret",
      "image": "models.svg",
      "description": "Slugs, timestamps, drafts and relations — small decisions in models.py that pay off months later.",
      "category": "Models",
      "tags": ['models', 'schema'],
      "author": "ahsharifi",
      "date": "Aug 13 - 6 min",
    },
    {
      "title": "How to use Django's built-in authentication",
      "image": "templates.svg",
      "description": "Django comes with a robust authentication system. Here's how to use it in your project.",
      "category": "Authentication",
      "tags": ['authentication', 'login', 'user'],
      "author": "ahsharifi",
      "date": "Aug 12 - 6 min",
    },
  ]

  recent_posts = sorted(data, key=lambda post: post['date'], reverse=True)[:3]

  return render(request, 'blogs/index.html', { "posts": data, "recent_posts": recent_posts })