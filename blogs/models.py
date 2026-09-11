from django.db import models

class Category(models.Model):
  title = models.CharField()
  description = models.TextField()

  def __str__(self):
    return self.title

class Blog(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  category_id = models.ForeignKey(Category, models.CASCADE, null=True)

  def __str__(self):
    return self.title