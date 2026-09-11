from django.db import models

class Category(models.Model):
  title = models.CharField()
  description = models.TextField()

  def __str__(self):
    return self.title

class Product(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(null=True)
  price = models.IntegerField()
  category_id = models.ForeignKey(Category, models.CASCADE, null=True)
  status = models.BooleanField()

  def __str__(self):
    return self.title